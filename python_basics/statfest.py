""" Q1:Write a Python program named mean_variance which takes a list of numbers 
as input and returns the mean and variance of the numbers (rounded to 2 decimals). 
You are not allowed to use any built-in statistics module."""

def mean_variance(lst):
    sum=0
    n=len(lst)
    for i in range(n):
        sum+=lst[i]
    am=sum/n    
    print(f"mean is : ",am)
    
    s_dev=0
    ss=0
    for i in range(n):
        s_dev=(lst[i]-am)**2
        ss+=s_dev
    print(f"sample variance is {ss/(n-1)}")
        
lst=[1,2,3,4,5]  
mean_variance(lst)  


""" Write a Python function probability_heads that takes the number of coin tosses n 
and returns the probability of getting exactly half heads."""

def pro_heads(n):
    if n % 2 !=0:
        return 0
    
    def fact(num):
        f=1
        for i in range(1,num+1):
            f*=i
        return f

    k=n//2
    p=0.5
    ncr= fact(n)//(fact(k) * fact(n-k))  

    prob= ncr * (p**k) * ((1-p) **(n-k)) 
    return prob

print(pro_heads(4))


"""Q3: Write a Python program series_identifier that determines 
whether a given numeric sequence is arithmetic, geometric,fibonacci or neither."""

def series_identifier(seq):
    if len(seq) < 3:
        return "Not enough elements"

    # Check Arithmetic
    is_arithmetic = True
    diff = seq[1] - seq[0]
    for i in range(1, len(seq)):
        if seq[i] - seq[i-1] != diff:
            is_arithmetic = False
            break

    # Check Geometric
    is_geometric = True
    if seq[0] == 0:
        is_geometric = False
    else:
        ratio = seq[1] / seq[0]
        for i in range(1, len(seq)):
            if seq[i-1] == 0 or seq[i] / seq[i-1] != ratio:
                is_geometric = False
                break
    
    #check fibonacci
    is_fibonacci= True
    for i in range(2,len(seq)):
        if seq[i] !=(seq[i-1]+ seq[i-2]):
            is_fibonacci=False
            break

    # Decide
    if is_arithmetic:
        return "Arithmetic Series"
    elif is_geometric:
        return "Geometric Series"
    elif is_fibonacci:
        return "fibonacci series"
    else:
        return "unknown"

# Example Usage:
nums=[0,1,1,2,3,5,8,2]
print(series_identifier(nums))



"""Q4. Write a Python function named correlation_coefficient(x, y) 
that calculates the Pearson correlation coefficient between two lists x and y."""

import math
def corr_coefficient(x,y):
    n=len(x)
    sumx=0
    sumy=0
    for i  in range(n):
        sumx+=x[i]
        sumy+=y[i]
    amx=sumx/n
    amy=sumy/n
   
    s_devx=0
    s_devy=0
    s_prod=0
    for i in range(n):
        devx=x[i]-amx
        devy=y[i]-amy
        s_devx+=devx**2
        s_devy+=devy**2
        s_prod+=(devx*devy)
    return s_prod/math.sqrt(s_devx*s_devy) 

x=[1,2,3,4,5]
y=[3,4,5,6,7]
print(corr_coefficient(x,y))



"""Q5. Write a Python program matrix_diagonal_sum that takes
  an n×n matrix and finds the sum of both diagonals."""

import numpy as np
def matrix_diagonal_sum(v):
    n=len(v)
    sum_d=0
    sum_sec_diagonal=0
    for i in range(n):
        for j in range(n):
            if i==j:
                sum_d+=v[i,j]

            if i+j==n-1:
                sum_sec_diagonal+=v[i,j]
                
    print('sum of first diagonal is',sum_d)
    print('sum of second diagonal is',sum_sec_diagonal)

v=np.array([[1,2,3],[4,5,6],[7,8,9]])            
matrix_diagonal_sum(v)


"""qs from matrix"""
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])  
n=len(matrix)

#sum of main diagonal--yk

#transpose a matrix
transposes=[[0 for _ in range(n)] for _ in range(n)] #if we dont use numpy(built n*n empty matrix)

transpose=np.zeros((n,n), dtype=int)

for i in range(n):
    for j in range(n):
        transpose[j,i]=matrix[i,j]


#matrix multiplication
B=np.array([[9,8,7],[6,5,4],[3,2,1]])
c=np.zeros((n,n), dtype=int)
for i in range(n):
    for j in range(n):
        total=0
        for k in range(n):
            total+=matrix[i,k]* B[k,j]

        c[i,j]=total
print(c)
 

#max value
max_value=matrix[0,0]
row=0
col=0

for i in range(n):
    for j in range(n):
        if matrix[i,j]> max_value:
            max_value=matrix[i,j]
            row,col=i,j
print(max_value, "at", row,col)            
 

#check if symmetric
def symmetric(v):
    is_symmetric=True

    for i in range(n):
        for j in range(n):
            if matrix[i,j] != matrix[j,i]:
                is_symmetric=False
                break

    if is_symmetric:
        result='symmetric'
    else:
        result='not symmetric'
    return result

print(symmetric(matrix))

#count element greater than mean
total=0
count=0
for i in range(n):
    for j in range(n):
        total+=matrix[i,j]
mean=total/(n*n)
for i in range(n):
    for j in range(n):
        if matrix[i,j]> mean:
            count+=1
print(count)

#each row and column sum
for i in range(n):
    row_sum=0
    for j in range(n):
        row_sum+=matrix[i,j]

for j in range(n):
    col_sum=0
    for i in range(n):
        col_sum+=matrix[i,j]
    print(col_sum)    





#Q6. Write a Python program mode_identifier which takes a list of integers 
# and returns their mode without using any built-in function.
import numpy as np
def mode_identifier(v):
    n=len(v)
    max_count=0
    mode=None
    for i in range(n):
        count=0        
        for j in range(n):
            if v[i]==v[j]:
                count+=1
        if count > max_count:
            max_count=count
            mode=v[i]
    return mode

print(mode_identifier(np.array([2,2,3,4,5,5,3,2])))        



#Q7. Write a Python program z_score which calculates the z-score for each element in a given list.
import math
import numpy as np
def z_scores(v):
    n=len(v)
    sum=0
    for i in range(n):
        sum+=v[i]
    mean=sum/n

    ss=0
    for i in range(n):
        ss+=(v[i]-mean)**2
    standard_dev=math.sqrt(ss/n)
    
    z_scores=[]
    for i in range(n):
        z=(v[i]-mean)/standard_dev
        z_scores.append(z)
    return z_scores

print(z_scores(np.array([10, 20, 30, 40, 50])))    



#Q8. Write a Python program random_sampler which generates n random samples 
# between 1 and 100 and computes their mean and standard deviation.
def random_sampler(n):
    sample=np.random.randint(1,100, size=n)

    sum=0
    for i in range(n):
        sum+=sample[i]
    mean=sum/n
    print(mean)
    ss=0
    for i in range(n):
        ss+=(sample[i]-mean)**2

    standard_dev=math.sqrt(ss/n)
    return standard_dev

print(random_sampler(10))



#Q9. Write a Python program data_cleaner that removes missing (None or NaN) values from a given list.
def data_cleaner(v):
    lst=[]
    for x in v:
        if x is not None and x==x:
            lst.append(x)
    return lst
v=[None,23,3,22,34,None, float('nan'), 34]
print(data_cleaner(v))


#Q10. Write a Python function frequency_table that returns a dictionary showing frequency of each unique element from a list.
def frequency_table(v):
    n=len(v)
    dct={}
    for i in range(n):
        count=0
        for j in range(n):
            if v[i]==v[j]:
                count+=1
            dct.update({v[i] : count})
    return dct

print(frequency_table([12,23,2,12,2,12,22]))           


#Q11. Write a Python program linear_regression that takes lists x and y as input
# and computes slope (β₁) and intercept (β₀) of the simple linear regression line.

def linear_regression(x,y):
    n=len(x)
    sumx=0
    sumy=0
    for i in range(n):
        sumx+=x[i]
        sumy+=y[i]
    amx=sumx/n
    amy=sumy/n

    ssx=0
    s_prod=0
    for i in range(n):
        ssx+=(x[i]-amx)**2
        s_prod+=(x[i]-amx)*(y[i]-amy)

    slope=s_prod/ssx
    print("slope is :", slope)

    intercept=amy-(slope*amx)
    print("the intercept is : ", intercept)
    return

linear_regression([1, 2, 3, 4, 5], [2, 4, 5, 4, 5])


#Q12. Write a Python program matrix_transpose that takes a 2D list (matrix) as input and prints its transpose.

def mat_transpose(matrix):
    n=len(matrix)
    n_matrix=np.zeros((n ,n ), dtype=int)
    for i in  range(n):
        for j in range(n):
            n_matrix[i,j]=matrix[j,i]
            
    return n_matrix
mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat_transpose(mat))        


#Q13. Write a Python program sum_nd_even which takes a general m×n matrix and returns the sum of non-diagonal even numbers.
def sum_nd_even(matrix):
    n=len(matrix)
    sum_m=0
    for i in range(n):
        for j in range(n):
            if i!=j and matrix[i,j] % 2==0:
                sum_m+=matrix[i,j]
    return sum_m

print(sum_nd_even(np.array([[1,2,3],[4,5,6],[7,8,9]])))         


#Q14. Write a Python function simulate_dice which simulates rolling two dice 1000 times and 
# prints the relative frequency of each possible sum (2–12).
def simulate_dice():
    counts={i : 0 for i in range(2,13)}
     
    for _ in range(1000):
        die1=np.random.randint(1,7)
        die2=np.random.randint(1,7)
        total=die1+die2
        counts[total]+=1

    for total in range(2,13):
        rel_freq=counts[total]/1000
        print(f"{total} \t {rel_freq: .3f}")
    
simulate_dice()


#Q15. Write a Python program outlier_detector which finds values in a list that are more than 2 standard deviations away from the mean.
def outlier_detector(data):
    # Step 1: Calculate mean
    n = len(data)
    total = 0
    for x in data:
        total += x
    mean = total / n

    # Step 2: Calculate standard deviation
    variance_sum = 0
    for x in data:
        variance_sum += (x - mean) ** 2
    std = (variance_sum / n) ** 0.5

    # Step 3: Detect outliers
    outliers = []
    for x in data:
        if abs(x - mean) > 2 * std:
            outliers.append(x)

    print("Mean:", mean)
    print("Standard Deviation:", std)
    print("Outliers:", outliers)

# Example
data = [10, 12, 13, 12, 11, 50, 9, 10, 8, 100]
outlier_detector(data)



#Q16. Write a Python function variance_matrix that computes the variance for each column of a numeric 2D list.
def variance_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    variances = []

    for j in range(cols):          # for each column
        # Step 1: Calculate column mean
        col_sum = 0
        for i in range(rows):
            col_sum += matrix[i][j]
        mean = col_sum / rows

        # Step 2: Calculate variance for this column
        variance_sum = 0
        for i in range(rows):
            variance_sum += (matrix[i][j] - mean) ** 2
        variance = variance_sum / rows

        variances.append(variance)

    print("Column-wise Variance:", variances)

# Example
data = [
    [10, 20, 30],
    [15, 25, 35],
    [20, 30, 40],
    [25, 35, 45]
]
variance_matrix(data)



#Q17. Write a Python function normal_pdf(x, μ, σ) to compute the probability density of a normal distribution.
def normal_pdf(x, mu, sigma):
    # Formula: (1 / (σ√(2π))) * e^(-(x - μ)² / (2σ²))
    part1 = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    result = part1 * exponent
    return result

# Example
print(normal_pdf(1, 0, 1))  # For x=1, μ=0, σ=1


