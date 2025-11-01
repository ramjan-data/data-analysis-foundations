import numpy as np
#reshaping
arr=np.array([3,4,5,5,5,9])  
reshaped_arr=arr.reshape(2,3) #1d to multi dimentional array 
print(reshaped_arr)

#-1 reshaping( numpy auto calc columns)
ar1=np.arange(12)
a_reshape=ar1.reshape(3,-1)  #auto calculated the columns(3,4)
print(a_reshape)

#multi dimentional array  to 1d
#.ravel--> return a view,    .flatten--> return a copy
arrr=np.array([[2,3,4],[2,3,3],[4,5,6],[4,3,2]])
print(arrr.ravel())
print(arrr.flatten())

#TRANSPOSE
arrr=np.array([[2,3,4],[2,3,3],[4,5,6],[4,3,2]])
print(arrr.T)  #shape (4,3) to (3,4)

#stacking
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.hstack([a,b]))   #[1,2,3,4,5,6]
print(np.vstack([a,b]))   #[[1,2,3],[4,5,6]]
print(np.dstack([a,b]))   #[[[1,4],[2,5],[3,6]]
#try 2d arrays

#splitting arrays
a=np.arange(12).reshape(3,-1)
print(np.hsplit(a,2))  #splite into two parts along column
print(np.vsplit(a,3))  #splite into three parts along rows

scores = np.array([
    [85, 90, 88, 92],
    [78, 80, 75, 85],
    [92, 95, 96, 94],
    [70, 72, 68, 65],
    [88, 89, 85, 90],
    [95, 98, 97, 99]
])
# Split into two sets: first 3 & last 3 students
train, test = np.vsplit(scores, 2)
print("Train:\n", train)
print("Test:\n", test)

#tiling and repeating
arr = np.array([1,2,3])
print(np.tile(arr, 3))   # repeat [1 2 3] → [1 2 3 1 2 3 1 2 3]
print(np.repeat(arr, 2)) # repeat each element → [1 1 2 2 3 3]


#adding and removing dimensions
a=np.array([1,2,3])
print(a.shape)  #3,
b=a[:,np.newaxis]
print(b.shape)  #3,1--column vector
 #alternative of this
c=np.expand_dims(a, axis=0)
print(c.shape)   #(1,3)

#squeeze
a=np.array([[[1,2,3]]])
print(a.shape)   #1,1,3
d=np.squeeze(a)
print(d.shape)   #3,
