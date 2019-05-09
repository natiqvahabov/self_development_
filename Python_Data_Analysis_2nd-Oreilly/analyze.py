'''
Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991
'''

#Pandas initial release is 2008, Jan

import pandas as pd

'''
As Python is an interpreted programming language, in general most Python code will run substantially slower than code written in a compiled language like Java or C++. As programmer time is often more valuable than CPU time, many are happy to make this trade-off
'''

'''
Compiled Language: C, C++, Objective C
Interpreted Language: Php, JS
Hybrid: Python, Java, VB
'''

''' Python as Glue
Python uses C,C++, Fortran for LinearAlgebra, Fourier Transforms(frequency analyisis of signals), and other algorithms.
'''

'''
Python can be a challenging language for building highly concurrent, multithreaded applications, particularly applications with many CPU-bound threads. 
The reason for this is that it has what is known as the global interpreter lock (GIL), a mechanism that prevents the interpreter from executing more than one Python instruction at a time.
'''

'''
Beyond the fast array-processing capabilities that NumPy adds to Python, one of its primary uses in data analysis is as a container for data to be passed between algorithms and libraries. 
For numerical data, NumPy arrays are more efficient for storing and manipulating data than the other built-in Python data structures. Also, libraries written in a lower-level language, such as C or Fortran, can operate on the data stored in a NumPy array without copying data into some other memory representation.
'''

'''
dict?, list?, func? is object introspection. 
def addIntegers(a, b):
	'ADD two integers'
	return a+b

addIntegers? -> 'ADD two integers'
'''

import matplotlib.pyplot as plt
import numpy as np 
plt.plot(np.random.randn(20).cumsum())


'''
The Python language design is distinguished by its emphasis on readability, simplicity, and explicitness. Some people go so far as to liken it to “executable pseudocode.”
'''

'''
Every number, string, data structure, function, class, module, and so on exists in the Python interpreter in its own “box,” which is referred to as a Python object
'''

#
a = [1, 2, 3]
b = a
a.append(4)
print(b)

#
a = 4; b = "Hello"
print("a is {0}, b is {1}".format(type(a),type(b)))

#
'''Strings and tuples are immutable objects in python which means we cant change the value of any index after created '''

#
from datetime import datetime, date, time
dt = datetime.now()
day = dt.day; hour=dt.hour

#
''' Ternary Operators:  value = true-expr if condition else false-expr'''

'''
tuple is immutable object type
can't modify object or change size

a, b, *_ = (4,5,6)
_ -> [5,6]

list -> append, remove, pop, insert, extend, sort
list[::-1] sort list in different way. list[::2] -> index 0,2,4...

enumerate -> list = ["first", "second", "third"]
			 mapping = {}
			 for i,v in enumerate(list):
			 	mapping[i]=v

dict = {key1:value1, key2:value2}
dict.keys(), dict.values(), pop, del, update

immutability == hashability

set -> A set is an unordered collection of unique elements

nums = [1,2,3,4,5]
{num:num**2 for num in nums if num>3}
{4:16, 5:25}
'''

# lambda functions

'''display fullname of user'''
full_name = lambda name, surname : name.strip().title() + " " + surname.strip().title()
full_name("  natiq", "vahabov ")

''' sort authors with last name '''
authors = ["Isaac Asimov", "Ray Bradbury", "Douglas Adams", "Arthur s. Clarke"]
authors.sort(key = lambda surname: surname.split(" ")[-1].lower())
