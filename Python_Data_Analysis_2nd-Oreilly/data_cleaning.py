# Data Cleaning and Preparation
# there are also unix text-processing tools like sed or awk

# Handling Missing Data
'''
	Pandas uses the floating-point value NaN (Not a Number) to represent missing data. 
	We call this a sentinel value that can be easily detected
'''

series = pd.Series(['avocado','orange',np.nan])
series.isnull()
'''
0 	  False
1     False
2     True
dtype: bool>
'''

from numpy import nan as NA
data = pd.Series([1, NA, 3.5, NA, 7])
data.dropna()

data[data.notnull()]

# for DataFrame use how="all", axis=1 for not removing whole row and column if it contains NaN

# thresh for keep certain number observations
data = pd.DataFrame(np.random.randn(7, 3))
data.iloc[:3, 1]=NA
data.iloc[:2, 2]=NA
data.dropna(thresh=2)

# filtering out is not good practice for lots of time, so filling in is better option
df.fillna(data.mean())

# droping duplicates
data.drop_duplicates() or data.drop_duplicates(['column_name'])

# mapping 
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
   ....:                               'Pastrami', 'corned beef', 'Bacon',
   ....:                               'pastrami', 'honey ham', 'nova lox'],
   ....:                      'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}

lowercased = data['food'].str.lower()
data['animal'] = lowercased.map(meat_to_animal)

# replacing values
data.replace(-999, NA)

# renaming or updating the values

data = pd.DataFrame(np.arange(12).reshape((3,4)),
	   index = ['ohio', 'colorado', 'new york'],
	   columns = ['one', 'two', 'three', 'four'])

transform = lambda x: x[:4].upper()
data.index = data.index.map(transform)

# string, regex and etc.
