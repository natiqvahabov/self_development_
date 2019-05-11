# Data Wrangling: Join, Combine, Reshape

# Hierarchical Indexing: is an important feature of pandas that enables you to have multiple (two or more) index levels on an axis
data = pd.Series(np.random.randn(9),
   ...:                  index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
   ...:                         [1, 2, 3, 1, 3, 1, 2, 2, 3]])

data.index
data.unstack().stack()
data['b':'d']

data = pd.DataFrame(np.arange(12).reshape(3,4), index=[['a','a','b'],[1
    ...: ,1,2]], columns = ['a','b','c','d'])
data.index.names = ['key1', 'key2']
data.columns.names

data.sort_index(level='key2')
data.swaplevel('key1', 'key2')
data.sum(level='key1')

# merge DFs by using how option to inner, outer, left, right joins

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
   ....:                     'data1': range(7)})

df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
   ....:                     'data2': range(3)})
pd.merge(df1, df2)

# concatenation
s1 = pd.Series([0,1], index=['a','b'])
s2 = pd.Series([2,3,4], index=['c', 'd', 'e'])
s3 = pd.Series([5,6], index=['f','g'])

pd.concat([s1,s2,s3])