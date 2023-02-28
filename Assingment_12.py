#ANS = 1
"""
An exception is an event, 
which occurs during the execution of a program that disrupts the normal flow of the program's instructions. 
In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. 
An exception is a Python object that represents an error

the error is a critical issue that a normal application should not catch, 
while an exception is a condition that a program should catch.
"""
# ANS = 2
"""
When an exception occurred, 
if you don't handle it, 
the program terminates abruptly and the code past the line that caused the exception will not get executed.
"""
# a = 10
# 10/0 # This program give line error say line number 18 give error.but if i used here a try and except it will not give error on terminal 

# ANS = 3
"""
The try and except block in Python is used to catch and handle exceptions.
"""
# try:
#     f = open("text.txt" ," r")
#     f.write("Hey pw sir's how are you")
# except ValueError as e:
#     print(e)

# ANS = 4
"""
try:
       # Some Code
except:
       # optional block
       # Handling of exception (if required)
else:
       # execute if no exception
"""

try:
    f = open("file.txt" , " w")
    f.write("I wnat became a data scientist with domain knowalge of biotechnology")
except:
    print("If some error present in above code they print")
else:
    f.close()   
    
# B. Finally 
"""
finally:
      # Some code .....(always executed)
"""
try:
    f = open("file.txt" , " w")
    f.write("I wnat became a data scientist with domain knowalge of biotechnology")
except:
    print("If some error present in above code they print")
else:
    f.close() 
finally:
    print("This line excut above line give error or not")
    
# C. Raise 
"""
The raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user.
"""

a = 10
if not type(a) is str:
    raise TypeError(" This is not a valid syntex")


# ANS = 5
"""
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class. 
Here's the syntax to define custom exceptions, class CustomError(Exception):
pass try: ... except CustomError: ...

:= why do we need custom exception:
Becouse some time we need to define some boundries if ower in-put go byound this we need custom exception 
"""

class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
number = 18
try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")

# ANS = 6
"""
we not need to write a defferent code to give solution of question no. 6  
    
"""

class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
number = 18
try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")    
except InvalidAgeException:
    print("Exception occurred: Invalid Age")