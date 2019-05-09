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

arr = np.random.randn(7, 3)
arr*=2
arr[arr<0.5]=0

arr[[1,2]] # array of second and third row

#changing the columns order
arr = np.arange(32).reshape(8, 4)
arr[:, [3,2,1,0]]

#transposing , dot product array
arr.T
np.dot(arr.T, arr)

#unary ufanc
np.sqrt(arr)
np.modf(arr)
np.exp(arr)
# abs,fabs,square,log,ceil,rint ..

# Array-oriented programming
# sqrt(x^2+y^2)

arr = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(arr, arr)
z = np.sqrt(xs**2+ys**2)

x_arr = np.array([1.1, 1.2, 1.3, 1.4])
y_arr = np.array([2.1, 2.2, 2.3, 2.4])
cond = [True, False, True, True]
result = [(x if c else y) for x,y,c in zip(x_arr,y_arr,cond)] # [1.1, 2.2, 1.3, 1.4]
result = np.where(cond, xarr, yarr)

np.unique(arr)
np.sort(arr)
(arr>0).sum() # mean(), max(), min()

#saving and loding numpy array
np.save('some_array', arr)
np.load('some_array.npy')