#Dictionary
#Dictionaries are used to store data values in key:value pairs

info={
    "key":"value",
    "name": "ramjan",
    "age": 24,
    "names1" :["tirtha", "nahid" , "simantha"],
    "names2" :("tajrian", "pranto" ,"areeba"),
     "numbr" :96.5,
     23 : 2323
}
print(info)

#to print different key values
print(info["name"])
print(info["age"])

#to assign or add new
info["name"]="rakib"  #for changing name value
info["surname"]= "sajid"  #add something new
print(info)

#create a null  dict and add values later
null_dict={}
print(null_dict)
null_dict["name"]=["ramjan","tirtha"]
print(null_dict)


#nested dictionaries
student={
    "name":"tajrian",
    "subjects":{
        "phy":98,
        "chem":87,
        "math":77
    }
}
print(student)
print(student["subjects"])


"""dictionary method"""

#returns all keys
student.keys()
print(list(student.keys()))   #list of all keys
print(len(student.keys()))    #number of keys

#returns all values
print(student.values()) 
print(list(student.values()))  #list of student values

##returns all (key, val) pairs as tuples
print(student.items()) 

 #inserts the specified items
student.update({"city":"dhaka"}) 
print(student) 



"""SETS"""
collection={2 ,3, 6, 2, "rakib", "world", "world", 4}
print(collection)
print(type(collection))
print(len(collection))

empty_set=set()
print(type(empty_set))

'''SET METHOD---add,remove,clear,pop'''
#add__in this system we can add int,float,string,touple but not list,dict
nothing=set()
nothing.add(1)
nothing.add(2)
nothing.add("tajrian")
nothing.add(2)
print(nothing)

#remove(el)---removes the element
collection={2 ,3, 6, 2, "rakib", "world", "world", 4}
collection.remove(2)
print(collection)

#remove a random value
collection.pop()

#empty the set
collection.clear()
print(collection)
print(len(collection))

#union and intersection
set1={2,5,3,3,3,4}
set2={2,3,4,4,43,3}
print(set1.union(set2))
print(set1.intersection(set2))



#practice :  WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
#Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
 
marks={}
a=input("enter phy: ")
marks.update({"phy" :a})

b=input("enter chem: ")
marks.update({"chem" :b} )

c=input("enter math: ")
marks.update({"math" :c})
print(marks)



