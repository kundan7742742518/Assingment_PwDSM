# ANS = 1
"""
The class Exception and its subclasses are a form of Throwable that indicates conditions 
that a reasonable application might want to catch. 
The class Exception and any subclasses that are not also subclasses of RuntimeException are checked exceptions
"""

# ANS = 2
import inspect
def classtree(cls , indent = 0):
    print("_"*indent , cls.__name__)
    for subclass in cls.__subclasses__():
        classtree(subclass ,indent+3)
inspect.getclasstree(inspect.getmro(BaseException))
classtree(BaseException)

# ANS = 3
"""
ArithmeticError Exception is the base class for all errors that occur for numeric calculations. 
It is the base class for those built-in exceptions like: OverflowError, ZeroDivisionError, FloatingPointError
"""
#  ZeroDivisionError

try:
    a = 10
    10/0
except ZeroDivisionError as e:
    print(e)

# FloatingPointError

import math
try:
    print ('Control off:', math.exp(7))
    print ('Control on:', math.exp(10))
except FloatingPointError as e:
    print(e)
    
# ANS = 4

"""
Lookup Error acts as a base class for the exceptions that occur when a key or index used on a mapping 
or sequence of a list/dictionary is invalid or does not exists[ IndexError. KeyError.]
"""
# IndexError
x = [1, 2, 3, 4]
try:
    print(x[10])
except LookupError as e:
    print(f"{e}, {e.__class__}")
    
# KeyError
pylenin_info = {'name': 'Lenin Mishra',
                'age': 28,
                'language': 'Python'}
user_input = input('What do you want to learn about Pylenin==> ')

try:
    print(f'{user_input} is {pylenin_info[user_input]}')
except LookupError as e:
    print(f'{e}, {e.__class__}')

# ANS = 5
"""
Importerror:- Import error is the if any module is not exist 
occurs when the Python program tries to import module which does not exist in the private table.
this error occurs when you're trying to access or use a module that cannot be found.
"""
# ANS = 6
# use alwyes specific exception 
# print alwayes a valid msg 
# alwayes try to log 
# alwayes avoid to write a multiple exept handling
# prepare a proper a documentation 
# clean up all the resaurces