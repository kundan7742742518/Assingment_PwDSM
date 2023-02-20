# ANS = 1
# class vehicle:
    
#     def __init__(self,  name_of_vehicle, max_speed , average_of_vehicle):
#         self.name_of_vehicle = name_of_vehicle
#         self.max_speed = max_speed
#         self.average_of_vehicle = average_of_vehicle
                
# hoo1 = vehicle("sudan", 200 , 48)
# a  = hoo1.average_of_vehicle
# print(a)

# ANS 2
class parent_vehicle:
    
    def __init__(self,  name_of_vehicle, max_speed , average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

class child(parent_vehicle):
    
    def seating_capacity(self, capacity):

        return f"{self.name_of_vehicle} has a seating capacity of {capacity} passengers."
      
my_car = child("pulkit", 200, 100)
print(my_car.seating_capacity(5))

# ANS = 3

"""
Multiple inheritance is a feature of object-oriented programming 
where a subclass can inherit from multiple superclasses.
        """
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Mammal(Animal):
    def breathe(self):
        print(f"{self.name} is breathing.")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

class Bat(Mammal, Bird):
    def __init__(self, name):
        super().__init__(name)

    def echo_location(self):
        print(f"{self.name} is using echolocation to navigate.")

bat = Bat("Fruit Bat")
bat.eat()           
bat.breathe()       
bat.fly()           
bat.echo_location() 

# ANS = 4
"""
getters and setters are methods that are used to access and modify the values of instance variables in a class. 
Getters allow us to retrieve the value of an instance variable, 
while setters allow us to modify the value of an instance variable
        """
        
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age >= 0 and age <= 120:
            self.age = age
        else:
            print("Invalid age.")

person = Person("Alice", 25)
print(person.get_name())  
person.set_name("Bob")
print(person.get_name())  

print(person.get_age())  
person.set_age(30)
print(person.get_age())  
person.set_age(150)      

# ANS = 5
"""method overriding is a feature of object-oriented programming that allows a subclass to provide a 
different implementation of a method that is already defined in its superclass. 
Method overriding is used to provide more specialized behavior for a method in a subclass, 
while still inheriting the general behavior of the method from its superclass.

"""
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(5, 10)
print(rectangle.area())  # Output: 50

circle = Circle(5)
print(circle.area())     # Output: 78.5
   