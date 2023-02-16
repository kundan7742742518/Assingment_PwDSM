# ANS = 1
# def keyword is used to create a function.
def odd_number(n):
    lis = []
    for i in range(n+1):
        if i%2 != 0:
            lis.append(i)
    return lis
lis = 25
print(odd_number(lis))

# ANS = 2
"""
*args
The special syntax *args in function definitions in python is used to pass 
a variable number of arguments to a function.
"""
def number(*args):
    return args
n = 1,2,3,4,5,6
print(number(n))

"""
**kwargs
The special syntax **kwargs in function definitions in python is used to pass a keyworded, 
variable-length argument list. We use the name kwargs with the double star. 
The reason is that the double star allows us to pass through keyword arguments
"""
def number_12(**kwargs):
    print(kwargs)
        
number_12(first ="kundan", second = "jangir")
        
    
# ANS = 3
"""
An iterator is an object that contains a countable number of values. 
An iterator is an object that can be iterated upon, 
meaning that you can traverse through all the values. 
Technically, in Python, an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__().
"""
"""
The iterator object is initialized using the iter() method. 
It uses the next() method for iteration
"""
x = [2, 4, 6, 8, 10, 12, 14, 16,18, 20]
y = iter(x)
print(next(y)) # WE use loop also but loop function is not ask in question i think
print(next(y))
print(next(y))
print(next(y))
print(next(y))

# ANS = 4
"""
A generator is a special type of function which does not return a single value, 
instead, it returns an iterator object with a sequence of values. In a generator function, 
a yield statement is used rather than a return statement
"""
"""
yield keyword is used to create a generator function.   
"""
def even_number(n):
    lis = []
    for i in range(n+1):
        if i%2 == 0:
            lis.append(i)
    yield(lis)        
n = 10
for i in even_number(n):
    print(i)
    
# ANS = 5
def prime_number(n):
    for i in range(n):
        c = 0
        for j in range(1,i):
            if i%j == 0:
                c = c+1
        if c == 1:
            yield(i)
           
n = int(input("Enter a Number:-")) 
a = []
for i in prime_number(n):
    a.append(i)
x = iter(a)
for i in range(20):
    print(next(x))



