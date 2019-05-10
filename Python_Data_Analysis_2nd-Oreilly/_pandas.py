import pandas as pd
data = pd.read_csv('examples/exl.csv', sep=',', names='col1,col2,col3,col4', skiprows=[0,1], na_values=['NULL'])

pd.isnull(data)

# If you want to only read a small number of rows (avoiding reading the entire file), specify that with nrows:
pd.read_csv('examples/ex6.csv', nrows=5)

# To read a file in pieces, specify a chunksize as a number of rows:
chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)

# Load json
obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
              {"name": "Katie", "age": 38,
               "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""

import json
result = json.loads(obj)
siblings = pd.DateFrame(result['siblings'], columns=['name','age'])

# json.dumps, on the other hand, converts a Python object back to JSON
asjson = json.dumps(result)

# Import HTMl, XML in pandas
tables = pd.read_html('examples/fdic_failed_bank_list.html')
len(tables)
failures = tables[0]
failures.head()

# XML
from lxml import objectify
path = 'examples/performance.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',
               'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)

perf = pd.DataFrame(data)
perf.head()