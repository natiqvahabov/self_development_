''' Numpy uses C, C++, Fortran low level languages to store and manipulate data. Numpy is faster core python'''
import numpy as np
my_arr = np.arange(100000)
my_list = list(range(100000))

'''
%time for _ in my_arr: my_arr *= 2 // 12 ms
%time for _ in my_list: my_list *= 2 //994 ms
'''

rand_one_number = np.random.randn()
rand_n_number = np.random.randn(n)
rand_n_array = np.random.randn(n, n)

rand_n_array *= 10
rand_n_array.shape
rand_n_array.dtype
rand_n_array.ndim
np.zeros(10)
np.zeros(4, 6)
np.zeros(4, 6, 2) # 2 times
np.arange(10)

#casting int64 ndarray to float64
arr = np.array([1, 2, 3, 4])
arr.dtype # np.array int64
arr = arr.astype(np.float64)
arr.dtype # np.array float64

#condition in nparray
names = np.array(['natiq', 'ali', 'elcin', 'natiq', 'nail'])
data = np.random.randn(5, 4)
cond = names == "natiq"
data[cond] # -> True rows 
data[~cond] # -> False rows






