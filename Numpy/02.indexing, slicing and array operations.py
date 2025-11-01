import numpy as np

#indexing 1d array
arr=np.array([30,40,50,53,55,98])
print(arr[0])
print(arr[3])
print(arr[-1])

#indexing 2d array
ar=np.array([[2,3,4],[1,2,1],[9,8,7]])
print(ar[0,0])  #row 0, column 0--(2)
print(ar[1,2])  #row 1 , column 2--(1)
print(ar[-1,-1])  #last row n column--(7)
#indexing 3d-do it yourself  arr[depth,row, col]

#slicing 1d array----[start,stop,step]
arr=np.array([30,40,50,53,55,98])
print(arr[1:3])
print(arr[3:])
print(arr[0:5:2])
print(arr[::-1])



#slicing 2d, array[row  slice,col slice]
ar=np.array([[2,3,4],
             [1,2,1],
             [9,8,7]])
print(ar[1:,1:3])   #[[2,1],[8,7]]
print(ar[0:2, 0:2])  #[[2,3],[1,2]]
print(ar[:,2])       #[4,1,7]

#fancy indexing----->selecting multiple element by index
arr=np.array([30,40,50,53,55,98])
print(arr[[0,2,4]])     #30 50 55


#where clause
arr = np.array([10, 20, 30, 40, 50])
indices = np.where(arr > 25)
print(indices)      # (array([2, 3, 4]),)
print(arr[indices]) # [30 40 50]


#filtering
print(arr[arr > 45])

#modifying subsets
arr=np.array([10,20,30,40,59])
arr[1:]=99
print(arr)   #[10,99,99,99,99]

#copy vs view
a=np.array([1,2,3,4])
b=a.copy()  #makes a copy of b
b[0]=99
print(a)   #originial not change
print(b)
#view
a = np.array([1, 2, 3])
v = a.view()       # makes a view, shares data
v[0] = 99
print(a)  # [99  2  3]  <- original changed!
print(v)  # [99  2  3]
#slice create view
a = np.array([1, 2, 3, 4])
s = a[1:3]  # this is a view----s=a[1:3].copy()[we can do this too]
s[0] = 99
print(a)  # [ 1 99  3  4]


"""array operation"""
#arithmetic operations
a=np.array([1,2,3,4])
print(a+10)
print(a-10)
print(a**2)  #so on...

#comparison operation
b=np.array([10,20,30])
print(b>25)  #false, false, true
print(b==20) #false ,true, false

#logical operations
a = np.array([10, 20, 30, 40])
print(np.logical_and(a > 10, a < 40))  # [False  True  True False]
print(np.logical_or(a == 10, a == 40)) # [ True False False  True]
print(np.logical_not(a > 25))          # [ True  True False False]


#broadcasting
a=np.array([[1,2,3],[4,5,6]])
b=np.array([10,20,30])
print(a+b)  #[[11,22,33],[14,25,36]]
c=np.array([[10],[20]])
print(a+c)   #[[11,12,13],[24,25,26]]


#aggregations
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(np.sum(arr))          # 21
print(np.mean(arr))         # 3.5
print(np.std(arr))          # 1.707...
print(np.var(arr))          # 2.916...
print(np.min(arr))          # 1
print(np.max(arr))          # 6
print(np.argmin(arr))       # index of smallest (0)
print(np.argmax(arr))       # index of largest (5)
print(np.percentile(arr,50))
print(np.cumsum(arr))
print(np.prod(arr))


#axis concept
print(np.sum(arr,axis=0)) #column wise [5,7,9]
print(np.sum(arr,axis=1)) #row wise [6,15]

#rounding
arrr=np.array([12.3322, 22.32145])
print(np.round(arrr, 2))
print(np.floor(arrr))

#Universal function
x = np.array([1, 2, 3, 4, 5])
print(np.sqrt(x))    # square root
print(np.exp(x))     # e^x
print(np.log(x))     # natural log
print(np.log10(x))   # log base 10
print(np.sin(x))     # sine
print(np.cos(x))     # cosine
print(np.abs([-1, -2, 3]))  # absolute values


#sorting and search
arr = np.array([4, 1, 7, 3])
print(np.sort(arr))          # [1 3 4 7]
print(np.argsort(arr))       # indices → [1 3 0 2]
print(np.argmax(arr))        # index of max → 2
print(np.argmin(arr))        # index of min → 1

