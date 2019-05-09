''' Numpy uses C, C++, Fortran low level languages to store and manipulate data. Numpy is faster core python'''
import numpy as np
my_arr = np.arange(100000)
my_list = list(range(100000))

%time for _ in my_arr: my_arr *= 2
%time for _ in my_list: my_list *= 2
