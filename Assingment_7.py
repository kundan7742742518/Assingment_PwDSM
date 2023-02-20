ANS = 1
def password_v_i(password):       
    if (len(password) > 10):
        lowercase = False
        uppercase = False
        special = False
        num     = False
        for i in password:
            if i.isdigit():
                num = True
            if i.islower():
                lowercase = True
            if i.isupper():
                uppercase = True
            if i.isalnum():
                special = True
        return ("valid password")
    else:
        return ("invalid password")
        
St = "kundanJ"
print(password_v_i(St))

ANS = 2
# FIRST
lis = ["Kundan","jangir","pulkit"]
lis1 = "j"
x = list(filter(lambda x: x.startswith(lis1),lis))
print(x)
# Second
a = ["123","a12b","abc", "ab@"]
x = list(filter(lambda x : x.isnumeric() , a))
print(x)

# Thard 
c = [("mango",99),("orange",80), ("grapes", 1000)]
v = sorted(c, key=lambda x : x[1])
print(v)

# forth
a = [pow(x,1/2) for x in range(1,11)]
print(a)

# fifth
roots = [pow(x, 1/3) for x in range(1, 11)]
print(roots)

# six
number = 7
result = lambda x: x % 2 == 0
print(result(number))

# siven
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 != 0, numbers))
print(result)

# eught 

numbers = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, 0]
positive = [x for x in numbers if x >= 0]
negative = [x for x in numbers if x < 0]
