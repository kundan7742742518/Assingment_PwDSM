"""
ANS = 1
class: a class describes the contents of the objects that belong to it: 
it describes an aggregate of data fields (called instance variables), 
and defines the operations (called methods). o
bject: an object is an element (or instance) of a class; 
objects have the behaviors of their class.
"""
# class ku:   # this is the class
#     def kund(felf):
#         print("Wellcome PWskills")
        
# a = ku()       # SO here [a] is the object 
# x = a.kund()  

"""
ANS = 2
Inheritance, 
Polymorphism, 
Encapsulation  
Abstraction
"""

"""
ANS = 3
All classes have a function called __init__(), 
which is always executed when the class is being initiated.
"""
# class persion:
#     def __init__(self , name ,age):
#         self.name = name
#         self.age = age

# x = persion("kundan" , 26)
# a = x.name
# print(a)

"""
ANS = 4
The self variable is used to represent the instance of the class.
"""
"""
ANS = 5
Inheritance is a mechanism in which one class acquires the property of another class.
"""
# single inheritance 

class Parent:
    def func1(self):
        print("This function is in parent class.")
 
 
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
 
 
# Driver's code
object = Child()
object.func1()
object.func2()

# Multiple Inheritance

class Grandfather:# Base class

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername


class Father(Grandfather): # Intermediate class
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername

		# invoking constructor of Grandfather class
		Grandfather.__init__(self, grandfathername)

class Son(Father):# Derived class
	def __init__(self, sonname, fathername, grandfathername):
		self.sonname = sonname

		# invoking constructor of Father class
		Father.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)


# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()

# Hierarchical Inheritance: 
  
# Python program to demonstrate
# Hierarchical inheritance


# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class1


class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")

# Derivied class2


class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")


# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# hybride ingeritence 

# Python program to demonstrate
# hybrid inheritance


class School:
	def func1(self):
		print("This function is in school.")


class Student1(School):
	def func2(self):
		print("This function is in student 1. ")


class Student2(School):
	def func3(self):
		print("This function is in student 2.")


class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()
