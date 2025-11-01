import numpy as np
a=np.array([1, 3, 6])
print(a)
print(type(a))

#minimum dimentional
a=np.array([1, 3, 6, 7, 8, 9], ndmin=2)  #ndmin means minimum dimentions
print(a)

#2d array
b=np.array([[3,4,5],
           [4,5,9],
           [6,7,8]])
print("2d array\n",b)

#dtype parameter
c=np.array([1,2,3], dtype= complex)
print("complex datatype\n",c)

#multi dimentional array
#matrix
matrix=np.array([[1,2,3],
                [3,4,5]])
print(matrix) 


"""special arrays"""
#zeros array---np.zeros(shape)
z_arr=np.zeros((2,3))
print("zeros array\n",z_arr)

#np.ones(shape)
ones_array=np.ones((2,4))
print("ones array\n",ones_array)

#np.full(shape,value)
filled_array=np.full((2,3),9)
print("custom fill\n",filled_array)

#np.empty(shape)--can be garbage value
empty_arr=np.empty((2,3))
print("garbage value\n", empty_arr)

#creating identity matrices---np.eye(size)
i_array=np.eye(3,3)
print("identity matrices\n",i_array)

#creating sequences of numbers in numpy----np.arange(start,stop,step)
arr=np.arange(1,11,3)
print("arranging values\n",arr)

#linear spaced---np.linspace(start,stop,number of values)
l_arr=np.linspace(0,1,5)
print("linear spaced\n",l_arr)



"""attributes of an array"""
aa=np.array([[2,3,4,5],[2,3,1,2]])
print(aa.ndim)  #dimentions
print(aa.shape)  #shape
print(aa.size)   #total elements
print(aa.dtype)  #data types
print(aa.itemsize) #size of one elements in bytes
print(aa.nbytes)  #total memory

#converting datatypes
arr=np.array([1.2,3.4,4.3,44.3])
arr2=arr.astype(int)
print(arr2)

