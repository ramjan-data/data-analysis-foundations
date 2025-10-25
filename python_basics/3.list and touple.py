#make a list
marks=[91, 65, 67.5, 67, 78]
print(marks)
print(len(marks))    #length of marks
print(marks[3])      #indexing 
print(type(marks))   #type -list
 
#we can use different types of data in a list
students=['rakib', 94.5, 17, "class-8", "pekua"]
print("personal info:",students[0])

#change the name rakib to rafi at index 0
students[0]="rafi"
print(students)

#list_slicing
marks=[45,67,87,67.6]
print(marks[1:4])
print(marks[0:])


'''LIST METHOD'''

list1=[3,4,2,1]

#add value in last
list1.append(6)

#ascending order
list1.sort() 

#descending order
list1.sort(reverse=True)

#reverse() --reverses list
list1.reverse()

#insert an item at a specifiq row
list1.insert(1,8)

#remove(x)--removes the first occurance of x
list1.remove(2)

#pop() --removes elements at index
list1.pop(1)

#clear()--removes all items
list1.clear()




'''TOUPLE'''
tup=(2, 1, 3, 2,4)
print(type(tup))
print(tup[0])

tup1=(1,)
print(tup1)
print(type(tup1))
print(tup1[1:3])

#returns index of first occurrence
tup.index(2) 

#counts total occurrences 
tup.count(2)  



#practice: WAP to ask the user to enter names of their 3 favorite movies & store them in a list
listt=[]
a1=input("enter the name of movie1:")
a2=input("enter the name of movie2:")
a3=input("enter the name of movie3:")
listt.append(a1)
listt.append(a2)
listt.append(a3)
print(listt)


#check palindrome
list1=[1,2,1]
c_list1=list1.copy()
c_list1.reverse()
if c_list1==list1:
    print("pelindrome")
else:
    ("Not pelindrome")

list2=[1,2,3]
c_list2=list2.copy()
c_list2.reverse()
if c_list2==list2:
    print("pelindrome")
else:
    print("Not pelindrome")

#string pelindrome
strr=input("enter the strings: ")
n_strr=""
for i in range(len(strr)-1,-1,-1):
    n_strr+=strr[i]
print(n_strr,end="")
print()    
if n_strr==strr:
    print("p")
else:
    print("n")

#max value of a list
list1=[3,4,5,2,3]
maxx=list1[0]
for i in list1:
    if i > maxx:
        maxx=i
print(maxx)         

#built in
print(max(list1))
print(min(list1))
print(sum(list1))
print(sorted(list1))


#remove duplicates
my_list=[1,2,3,2,1,4,5]
s=set()
un_list=[]
for i in my_list:
    if i not in s:
        s.add(i)
        un_list.append(i)
print(un_list) 

#removes duplicates but it also sort the list, be careful
my_list=[1,2,3,1,2]
u_list=list(set(my_list))
print(u_list)     