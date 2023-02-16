# ANS = 1
"""
Tuples contains a sequence of elements. 
The elements can be types, expressions, or aliases. 
The number and elements of a tuple are fixed at compile time and they cannot be changed at run time. 
Tuples have characteristics of both structs and arrays.
"""
"""
yes , tuple is immutable 
"""

# ANS = 2
"""
count()
index()
Python has two built-in methods that you can use on tuples.

"""
x = (2,2,2,7,5,8,6)
a = x.count(2)
print(a)

x = (2,7,5,8,6)
a = x.index(8)
print(a)

"""
Tuple has only two in-built method becouse tuple is immutable.
Becouse of their immutablity tuple not perphorm manupulation and other function. 
"""

# ANS = 3
"""
Set   datatypes in python do not allow duplicate items.
"""

x =   [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
a = set(x)
print(a)

# ANS = 4
"""
update() adds all missing elements to the set on which it is called whereas set. 
union() creates a new set
"""
A = {2, 4, 5, 6}
B = {4, 6, 7, 8}
c = A.union(B)
print(c)

d = {2,5,8,9}
s = {1,8,10,11}
s.update(d)
print(s)

# ANS = 5

"""
Dictionary in Python is a collection of keys values, 
used to store data values like a map, 
which, unlike other data types which hold only a single value as an element.
"""
Dict = {1: 'k', 2: 'j', 3: 'p'}
print(Dict)
"""
A dictionary is an unordered and mutable
"""

# ANS = 6
# Yes, we create a nested dictionary
a = {"Kundan":"Jnagir","pulkit":"leuva","pulkit_friend":{"pulkit_1":"vijeta","vindya":"sreerupa"}}
print(a)

ANS = 7
dct1 =  {'language' : 'Python', 'course': 'Data Science Masters'}
x = dct1.setdefault('key', ['Python', 'Machine Learning', 'Deep Learning'])
print(dct1)

ANS = 8 
'''
dictionary has three in-built method [key, value , items]
'''
dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}
x = dict1.keys()
a = dict1.values()
c = dict1.items()
print(x)
print(a)
print(c)