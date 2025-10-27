#LOOP-Loops are used to repeat instructions. 
#WHILE_LOOP

#print 'hello' five times
i=1
while i<=5:
    print("hello")
    i+=1

#practice
i=1
while i<=10:
    print("heydude", i)
    i+=2


#print number 1 to 5
i=1
while i<=5:
    print(i)
    i+=1
print("loop ended")    

#5 to 1
i=5
while i>=1:
    print(i)
    i-=1
print("ended")  

#Print the multiplication table of a number n.
n=int(input("multiplication table for: "))
i=1
while i<=10:
    print(f"{n} * {i} = {n*i}")
    i+=1


#Print the elements of the following list using a loop..
nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(nums):
    print(nums[idx]) #nums[0],nums[1], nums[2]... 
    idx+=1

#Search for a number x in this tuple using loop
tup=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(tup):
    if(tup[i]==x):
        print("FOUND at IDX",i)
    i+=1

#break:used to terminate the loop when encountered.
i=1
while i<=5:
    print(i)
    if(i==3):   #will stop the loop when i==3
        break
    i+=1
print("lood end")  

#continue
i=1
while i<=7:
    if(i==3):    
        i+=3     #skip 3,4,5
        continue 
    print(i)
    i+=1

#odd numbr
i=1
while i<=20:
    if(i%2==0):  #even(i% != 0)
        i+=1
        continue
    print(i)
    i+=1
print("END OF WHILE")





"""FOR LOOP"""
students=["tajrian",38, "gopalganj"]
for val in students:
    print(val)

tup=(6,3,4,4,5,5,6,44)
for val in tup:
    print(val)

srting="ramjan"
for char in srting:
    print(char)

#range(start,stop, step)
seq=range(5)   
print(seq[0]) 
print(seq[2])
for i in seq:
    print(i)

n=range(10)
for i in n:
    print(i)


for  i in range(10): #range(stop)
    print(i)
for  i in range(2,10):  #range(start,stop)
    print(i)
for  i in range(2,10,3):      #range(start,stop,step)
    print(i)

#print 10 to 1
for i in range(10,0,-1):
    print(i) 

#pass statement : pass is a null statement that does nothing. It is used as a placeholder for future code.    
for i in range(10,0,-3):  
    pass #empty
print("nothing")

#WAP to find the sum of first n numbers. (using for and while)
n=10
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#while
n=10
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print("sum=",sum)

#factorial for nth
n=10
i=1
fact=1
while i<=n:
    fact*=i
    i+=1
print("factorial is ",fact)

n=10
fact=1
for i in range(1,n):
    fact*=i
print('factorial of 10 by for loop is', fact)    

#practice using for loop
#wap to print 1 to 5
for i in  range(1,6):
    print(i, end=" ")

print(" ")    

#square of -1 to -5
for i in range(-5,0):
    square=pow(i,2)
    print(square, end=" ")

print(" ")

#even number 1 to 10
for i in range(1,11):
    if i%2==0:
        print(i)

#calculate sum of numbers from 1 to 10
sum=0
for i in range(1,11):
    sum+=i
print(f'sum of total {sum}')       

#reverse the word "python"
word="python"
for i in range(len(word)-1,-1,-1):
    print(word[i],end=" ")

#count vowels in a string
vowels="aeiou"
word="educations"
count=0
for i in range(len(vowels)):
    for j in range(len(word)):
        if vowels[i]==word[j]:
            count+=1
print("vowels count:",count)        

#print fibonacci sequence up to 10 terms------->> 0 1 1 2 3 5  13 21 34
#(a,b input),(a+b),(variables update),(output)
a, b= 0,1
for i in range(10):
    print(a, end=" ")
    a,b=b, a+b
   

#cheak if a number is prime or not
num=7
is_prime=True
for i in range(2,int(num**.5)+1):
    if num % i==0:
        is_prime=False

if is_prime and num>1:
    print(num,"is a prime number")  
else:
    print(num, "is not a prime number")          


# Write a program to greet all the person names stored in a list ‘l’ and which starts with s
l=["harry","soham",'sachin','rahul']
for items in l:
    for start in items:
        if start[0]=='s':
            print("congratulations",items)
        else:
            ("better luck next time")     

