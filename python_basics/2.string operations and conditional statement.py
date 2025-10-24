"""string operations"""
#concatenation
a='hello'
b='world'
concate=a+b
print(concate)

#length of string
a="hello world"
length=len(a)
print(length)  #11

#indexing(0,1,2,3...)
strr="Dhaka university"
n=strr[3]
print(n) #k

#slicing---str[start:stop:skip]
strr="Dhaka university"
print(strr[6:8])
print(strr[6:])
print(strr[::2])

#negative slicing
strr='tara'
print('revers of tara is:',strr[::-1])

#string functions
str='iam a coder.'
print(str.endswith('er.'))  #returns true if string ends with sub-string.
print(str.capitalize())     #capitalizes first char
print(str.replace('coder', 'programmer'))
print(str.find('am'))       #resturns 1st index of 1st occurrence
print(str.count('a'))       #counts the occurences


#conditional statements(if, elif,else)
#check if a man with age 21 can drive and vote or not
age=21
if(age >= 18):
    print("can drive and vote")
else:
    print("cant drive and cant vote")
    
#check the traffic control 
light="green"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("slow")
else:
    print("revers the road")   


#grade students based on marks
marks=int(input("enter the marks:"))
if(marks>=90):
    grade="A"
elif(marks<90 and marks>=80):
    grade="B"
elif(marks<80 and marks>=70):
    grade="C"
else:
    grade="fail"
print("the student result is:", grade)

##if there is any harry in post
post='hey bro i ws there for you ,haRry come back man'
post=post.lower() #Convert text to lowercase so it works even if user types 'harry' or 'HARRY'
if 'harry' in post:
    print("present")
else:
    print("absence")

#nested loop
age=33
if(age>=17):
    if(age>=80):
        print("can drive")
    else:
        print("cannot drive")    
else:
    print('cannot drive')

