import numpy as np
# ANS = 1
"""
List can store elements of different types, 
"but" arrays can store elements only of the same type.
"""
list_ = [ '1' , '2' , '3' , '4' , '5' ]
print(type(list_))
array_list = np.array(object = list_)
print(type(array_list))

# # ANS = 2
list_ = [ '1' , '2' , '3' , '4' , '5' ]
for i in list_:
    print(type(i), end= ' ')
    
array_list = np.array(object = list_)
for i in array_list:
    print(type(i), end = ' ')

# ANS = 3
"""
list_ :- contain all the str object 
if we introduce the dtype = int in this np.arry then list_ change in intiger.
"""
list_ = [ '1' , '2' , '3' , '4' , '5' ]
for i in list_:
     print(type(i), end= ' ')
array_list = np.array(object = list_, dtype = int)
for i in array_list:
    print(type(i), end = ' ')


# ANS = 4
num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
num_array = np.array(object = num_list)
shape_1 = np.shape(num_array)
size_1 = np.size(num_array)
print(shape_1)
print(size_1)


# ANS = 5
three_three = np.zeros((3,3))
shape_1 = np.shape(three_three)
size_1 = np.size(three_three)
print(three_three)
print(shape_1)
print(size_1)

# ANS = 6
five_five = np.identity(5 , dtype= "int")
print(five_five)
shape_1 = np.shape(five_five)
size_1 = np.size(five_five)
print(shape_1)
print(size_1)




