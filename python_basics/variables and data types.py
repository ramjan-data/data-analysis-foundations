#single line comment
"""
multi line
comment
 """



#variables and their data types
name='ramjan'
age=20
salary=2000.00
marital_status=False
a=None

print(name)         
print(type(name))   #string
print(type(age))    #integers    
print(type(salary)) #float
print(type(marital_status)) #boolean
print(type(a))      #None


'''OPERATORS'''
#arithmetic operators(+,-,*,/,%,**)
a=10
b=5
add=a+b  #addition
sub=a-b  #substraction
mul=a*b  #multiplication
div=a/b  #division
rem=a%b  #reminder
power=a**b #power
print(add)
print(sub)
print(mul)
print(power)

#comparison operators(==,!=,>,<,>=,<=)
a=50
b=30
print(a==b)  #False
print(a>=b)  #True

#assignment operator(=,+=,-=,*=,/=,%=,**=)
sum=0
i=5
sum+=i
print("sum:",sum) 

#logical operator(not,and,or)
c=40
d=10
print(not (c>d))  #False

val1=True
val3=False
print("and operator:",val1 and val3)  #False
print("or operator:",val1 or val3)    #True



#type conversion(automatically converts)
x=10
y=2.5
result=x+y
print(result)
print(type(result))   #float

#type casting(manually converts the data type)
x='100'
y=int(x)        #int,float, complex,str, tuple, list, set, dict...
print(y+10)  #110


#input by users
name=input("enter your name: ")
print('welcome',name)

#input with data types
name=str(input("enter your name: "))
age=int(input("enter your age: "))
salary=float(input("enter your salary: "))

print(f"welcome {name},\nas we can see, your age is {age} and your salary is {salary}.")

#Practice-1: Write a Program to input 2 numbers & print their sum.
a=int(input("enter value1: "))
b=int(input("enter value2: "))
sum=a+b
print('sum is',sum)

#practice-2:WAP to input side of a square & print its area.
a=int(input("enter value : "))
area=pow(a,2)
print("Area of the square is", area)

#practice-3: WAP to input 2 floating point numbers & print their average.
x=float(input("enter the value1: "))
y=float(input("enter the value2: "))
avg=(x+y)/2
print('the average is',avg)
