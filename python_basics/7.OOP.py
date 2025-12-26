# creating class
class Students:
    name="ramjan"

#objects
s1=Students()
print(s1.name)
s2=Students()
print(s2.name)


class Car:
    colour="blue"
    brand="marcedes"

car1=Car()
print(car1.colour)    
print(car1.brand)


#__init__ Function
class Students:
    def __init__(self):   #default constructors
        pass

    #parameterized constructors
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("adding new students in database")

s1=Students("tajrian",97)
print(s1.name, s1.marks)
s2=Students("tirtha",20)
print(s2.name, s2.marks)


#class and instance attributes
class Students:
    college_name="DU"                          #class attribute
    def __init__(self,name,marks):
        self.name=name                         #object attribute
        self.marks=marks
        print("adding new students in database")

    def welcome(self):
        print("welcome students", self.name)

    def gets_marks(self):
        return self.marks


s1=Students("tirtha",97)
print(s1.name, s1.marks)

s2=Students("pranto",20)
print(s2.name, s2.marks)

print(Students.college_name)
print(s2.college_name)

s1.welcome()
s1.gets_marks()
print(s1.gets_marks())

#practice
class student:
    def __init__(self, name,phy, chem, math):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.math=math

    def average(self):
        avg=(self.phy+self.math+self.chem)/3
        print('your average marks in these three subj is',round(avg,2))

s1=student('rakib', 98,96,90)
print('welcome mrs',s1.name)
s1.average()




#different method
class Students:
    def __init__(self,name, marks):
        self.name=name
        self.marks=marks

    @staticmethod      #using static method as decorator( we dont need to write 'self'.it work at class level)
    def welcome():
        print('Our journey begins here')


    def average(self):
        n=len(self.marks)
        sum=0
        for i in range(n):
            sum+=self.marks[i]
        avg=sum/n
        print(f'hello mr {self.name} your average marks is {avg}')


s1=Students('tony stark',[98,96,90])
s1.welcome()       
s1.average()

s1.name='iron man'   #we can change attribute
s1.average()






"""
    PILLAR OF OOPs :
                -abstraction
                -encaptulation 
                -inheritence
                -polymorphism
"""



"""Abstraction
        -hiding the implementation details of a class and only showing the essential features to the user"""

class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.acc=True
        self.clutch=True   
        print('car started..') 

car1=car()
car1.start()




"""encaptulation:
                wrapping data and function into a single unit(object)
                
"""

#practice--creat a bank acc
class account:
    def __init__(self, bal, acc):
        self.balance=bal
        self.acc_no=acc

    #debit method
    def debit(self,amount):
        self.balance-=amount
        print(f'Tk. {amount} was debited')
        print('total available balace is =', self.get_balanced())
    
    #credit method
    def credit(self, amount):
        self.balance+=amount
        print(f'tk. {amount} was credited')
        print('total available balace is =', self.get_balanced())

    def get_balanced(self):
        return self.balance

acc1=account(10000,'EM1000')
acc1.debit(1000)
acc1.credit(2000)




#part2

#del(use to delete object properties or object)
class student:
    def __init__(self, name):
        self.name=name

s1=student('karan')
print(s1.name)

# del s1      #object has been deleted
# print(s1)




#public--all we have done before it was public
#private (use __ before attribute )
class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.__password=acc_pass

    def reset_pass(self):
        print(self.__password)    

acc1=account(12345,'abcde')
acc1.reset_pass()

# print(acc1.password)     #we cant access beyond the class

#example-2
class person:
    __name='anonnymous'

    def __hello(self):
        print('hello person')

    def welcome(self):
        self.__hello()  

p1=person()
p1.welcome()




"""inheritence : when one class(child/derived)  derives the method & properties of another class (parents/base)
            -single
            -multi level
            -multi inheritence
"""
#single
class car:
    color='black'

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print('car stopped.')  

class toyotacar(car):
    def __init__(self,name):
        self.name=name

car1=toyotacar('fortuner')
car2=toyotacar('prius')

print(car1.name)
print(car1.start())
print(car2.color)




#multi level inheritence 
class car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print('car stopped.')  

class toyotacar(car):
    def __init__(self,brand):
        self.name=brand

class fortuner(toyotacar):
    def __init__(self, type):
        self.type=type

car1=fortuner('diesel')
car1.stop()
#so on.....


#multiple inheritence
class A:
    varA='welcome to class A'

class B:
    varB='welcome to class B'

class C(A,B):
    varC='welcome to class C'

c1=C()
print(c1.varB)




"""Super method"""

class car:
    def __init__(self, type):
        self.type=type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print('car stopped.')  

class toyotacar(car):
    def __init__(self,brand, type):
        super().start()                     #it'll call start fucntion
        super().__init__(type)
        self.brand=brand
        

car1=toyotacar('prius', 'electric')
print(car1.type)



"""class method"""

class person:
    name='ramjan'

    #def namechange(self,name):
        #person.name=name            #if we wrote self.name, it wont change anything
        

    @classmethod
    def namechange(cls, name):
        cls.name=name

    #or
    def changename(self, name):
        person.name=name 


    #or
    def chng_Name(self, name):
        self.__class__.name ='rahul'   

p1=person()
p1.namechange('tajrian')
print(p1.name)
print(person.name)




"""property decorator
                    -if need to chnage value
"""


class student:
    def __init__(self, phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+ self.chem+ self.math)/3) +'%'

    def percentages(self):
        self.percentage=str((self.phy+ self.chem+ self.math)/3) +'%'   
        return self.percentage

    @property
    def percentagess(self):
        return str((self.phy+ self.chem+ self.math)/3) +'%'
    
s1=student(97,98,99)
print(s1.percentage)

s1.phy=88
print(s1.percentages())

s1.phy=88
print(s1.percentagess)






"""Polymorphism : the same method name behaves differently depending on the object that called it.

                example:  1+2 #3
                        'apna' + 'college'  #concatenate(apnacollege)
                        [1,2] + [3,4]  #marge ([1, 2, 3, 4])

                        
Operator overloading: when the same operator is allowed to have different meaning according to the context.
operators and dunder functions : 
                                a+b  -> a.__add__(b)
                                a-b  -> a.__sub__(b)
                                a*b  -> a.__mul____(b)
                                a/b  -> a.__truediv____(b)
                                a%b  -> a.__mod____(b)
"""                                

#create a complex numbers class
class complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(f"{self.real} i + {self.img} j")

    def __add__(self, num2):
        NewReal=self.real + num2.real
        NewImg= self.img + num2.img
        return complex(NewReal, NewImg)

    def __sub__(self, num2):
        NewReal=self.real - num2.real
        NewImg= self.img - num2.img
        return complex(NewReal, NewImg)

    def __mul__(self, num2):
        NewReal=self.real * num2.real
        NewImg= self.img * num2.img
        return complex(NewReal, NewImg)    

num1=complex(1, 2)
num1.showNumber()   

num2=complex(3, 4)
num2.showNumber()

#addition
num3= num1 + num2
num3.showNumber()

#substraction
num3= num1 - num2
num3.showNumber()

#multiplication
num3=num1* num2
num3.showNumber()