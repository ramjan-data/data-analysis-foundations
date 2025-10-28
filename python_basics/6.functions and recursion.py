#PYTHON FUNCTION

#WAP to print sum of two values
def sum(a, b):
    s=a+b
    print(s)
    
sum(2,3) #call for function
sum(244,56)
sum(33,44)

#using return
def sum(a,b):
    return a+b
s=sum(33,44567)
print(s)


def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()    

#average of 3 numbers
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print("the avg is:",avg)
calc_avg(3,4,5)
calc_avg(3,4,9)


#square of a number
def square(a):
    sq=pow(a,2)
    return sq
print(square(5))


#default parameter:Assigning a default value to parameter, which is used when no argument is passed.
def default(a, b=2):
    return a*b
c=default(4,4)
d=default(3)
print(c)
print(f'default {d}')


#practice:WAF to print the length of a list
cities=["dhaka","bbb",'bb','ctg','slt','ctgg']
def length(lst):
    n=len(lst)
    return n

s=length(cities)
print(s)

#alternative
def length(lst):
    count=0
    for item in lst:
        count+=1
    print(count)    

length(cities)


# WAF to find the factorial of n. (n is the parameter)
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
a=calc_fact(20)
print(a)


#WAF to convert USD to tk. 
def transfer(usd):
    t=100
    print(f"{usd} USD= {usd*t} taka")
transfer(122)   



#nested
def outer():
    print("heyy")
    def inner():
        print("okay")
    inner()

outer() 


#reverse a string
def rev_string(str):
    n=len(str)
    for i in range(n-1,-1,-1):
        print(str[i], end="")

rev_string('heydude')


#take a list with numbers and return its  square values sum
def square_sum(lst):
    sq_sum=0
    for i in range(len(lst)):
        sq_sum+=(lst[i])**2
    print(sq_sum)
    return

square_sum([1,2,3,4,5])

#counting vowels on random text
def count_vowels(s):
    vowels="aeiou"
    count=0
    for i in range(len(s)):
        for  j in range(len(vowels)):
            if s[i]==vowels[j]:
                count+=1
    print(count)     
    return

count_vowels("heyybroeeee")


#number is prime or not
def is_prime():    
    n=int(input("enter the value: "))
    prime=True
    if n<=1:
        prime=False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                prime=False
                break
    print(prime) 
    return

is_prime()

#mean of a list number
def mean(lst):
    sum=0
    n=len(lst)
    for i in range(n):
        sum+=lst[i]
    return sum/n

lst=[12,2,3,4,2]
print(mean(lst))




#RECURSION
#want to print 5,4,3,2,1
def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
show(5) 

#return n!
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n *  fact(n-1)

print(fact(5))

#print n nutural number
def calc_sum(n):
    if n==0:
        return 0
    return calc_sum(n-1)+n
print(calc_sum(5))



print("lambdaaa func")
#lambda func
double=lambda x: x*2
cube= lambda x: x*x*x
avg= lambda x,y,z : (x+y+z)/3


print(double(5))
print(cube(5))
print(avg(3,4,5))