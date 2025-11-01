import numpy as np
A=np.array([[1,2],[3,4]])
b=np.array([9,7])
print(np.linalg.solve(A,b))  #solution of x,y
print(np.linalg.det(A))  #determinant of A
print(np.linalg.inv(A))   #inverse of A
print(np.linalg.eig(A))  #eigen vectors and eigen values
print(np.linalg.matrix_rank(A))  #rank
print(np.linalg.pinv(A))  #pseodu invers for non-square matrix
print(np.trace(A))
print(np.diag(A))  #diagonal
print(np.linalg.norm(A))  #magnitude

#matrix multiplications
ar=np.array([[1,2],[3,4]])
arr=np.array([[5,6],[7,8]])
print(np.matmul(ar,arr))
print(np.dot(ar,arr)) 
print(ar @ arr)  #all three do the same things

#transpose and conjugate transpose
ar=np.array([[1,2],[3,4]])
print(ar.T)
aa=np.array([[1+1j,2],[3,4]])
print(aa.conj().T)

#correlation and coveriance matrix
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
print("Covariance matrix:\n", np.cov(x, y))
print("Correlation matrix:\n", np.corrcoef(x, y))



# dataset: 6 students, 3 subjects
scores = np.array([
    [85, 90, 92],
    [78, 88, 80],
    [90, 92, 85],
    [72, 70, 75],
    [88, 85, 87],
    [95, 98, 97]
])

# 1. Subject means and std
print("Mean per subject:", np.mean(scores, axis=0))
print("Std per subject:", np.std(scores, axis=0))

# 2. Correlation between subjects
print("Correlation matrix:\n", np.corrcoef(scores.T))

# 3. Top student (highest average)
student_avg = np.mean(scores, axis=1)
print("Top student index:", np.argmax(student_avg))

# 4. Solve a linear system: predict weights for combining subjects
A = scores[:3,:]   # first 3 students' scores
b = np.array([260, 246, 267])  # target total scores
weights = np.linalg.lstsq(A,b,rcond=None)[0]
print("Subject weights (linear regression):", weights)


#random module
#uniform random  numbr(0 to 1)
a=np.random.rand()     #one random float between 0 and 1
b=np.random.rand(2,3)  #2x3 array of random floats between 0 and 1
print(a)
print(b)
# random floats from a uniform range
np.random.uniform(low=5, high=10, size=(2, 3))

#random integer
c=np.random.randint(1,10)           #one random integer between 1 and 10
d=np.random.randint(1,10,size=5)    #array of 5 random ints between 1 and 10
e=np.random.randint(1, 10, size=(2, 3))  #2d array
print(c)
print(d)

#random floats(normal distribution)
a=np.random.randn(3)  #3 random numbr from normal distribution(mean=0, std=1)
print(a)

#choose random element
arr = np.array([1, 2, 3, 4, 5])
np.random.choice(arr)     # pick one element randomly      
np.random.choice(arr, size=3, replace=True)   # pick 3 elements with replacement
np.random.choice(arr, size=3, replace=False)  # pick 3 elements without replacement

#suffle in-place
arr = np.array([10, 20, 30, 40])
np.random.shuffle(arr)
print(arr)  # arr is now shuffled


#permutation(returns a new suffled array)
arr = np.array([1, 2, 3, 4])
new_arr = np.random.permutation(arr)

#DISTRIBUTION
#normal(gaussian distrbution), loc=mean, scale=std, size=shape of output
np.random.normal(loc=0, scale=1, size=(2,3))

#binomial
np.random.binomial(n=10, p=0.5, size=5)  #repeated 5 times

#poisson
np.random.poisson(lam=3, size=10)

#exponential
np.random.exponential(scale=1.0, size=5)

#setting seed
np.random.seed(42)
print(np.random.rand(3))



#the new generating api
#the default_rng() method is faster, safer, and preferred for new code.
rng = np.random.default_rng()

rng.integers(1, 10, size=5)
rng.random((2,3))
rng.normal(0, 1, size=5)
rng.choice([1,2,3,4,5], size=3)

