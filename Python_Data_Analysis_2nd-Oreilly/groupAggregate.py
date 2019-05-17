'''Hadley Wickham, an author of many popular packages for the R programming language, 
	coined the term split-apply-combine for describing group operations.'''

import pandas as pd
import numpy as np

df = pd.DataFrame({
	'key1': ['a', 'a', 'b', 'b', 'a'],
	'key2': ['one', 'two', 'one', 'two', 'one'],
	'data1': np.random.randn(5),
	'data2': np.random.randn(5)
	})

'''
key1 key2     data1     data2
0    a  one -0.525498 -0.156302
1    a  two  0.179738  0.716692
2    b  one -1.847801 -0.693378
3    b  two  0.275600 -0.011464
4    a  one -0.608233  0.993777
'''

grouped = df['data1'].groupby(df['key1'])
grouped.mean()

means = df['data1'].groupby([df['key1'], df['key2']]).mean()
'''
key1  key2
a     one    -0.566865
      two     0.179738
b     one    -1.847801
      two     0.275600
'''

for name, group in df.groupby('key1'):
	print(name)
	print(group)

df.groupby('key1')['data1'] === df['data1'].groupby(df['key1'])

# We can fill the NA values using the group means like so
fill_mean = lambda g: g.fillna(g.mean())
data.groupby(group_key).apply(fill_mean)