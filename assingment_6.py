ANS = 1
def flate_list(list1):
    list2 =  []
    for i in list1:
        if type(i) == list or type(i) == tuple or type(i)  == set:
            for j in i:
              if type(j) == int:
                   list2.append(j)
        elif type(i) == dict:
            for a in i.keys():
                if type(a) == int:
                    list2.append(a)
            for b in i.values():
                if type(b) == int:
                    list2.append(b)
                if type(b) == list or type(b) == tuple:
                    for c in b:
                        list2.append(c) 
        else:
            if type(i) == int:
                list2.append(i)           
    product = 1
    for i in list2:
        product = product*i  
    return product

list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45, 
22, 61, 34)}, [56, 'data science'], 'Machine Learning'] 
print(flate_list(list1))   




# ANS = 2
# import string 
# lis1 = []
# for i in string.ascii_lowercase:
#     lis1.append(i)
# print(lis1)
# lis2 = []
# for i in string.ascii_lowercase[::-1]:
#     lis2.append(i)
# print(lis2)
# res = {lis1[i]: lis2[i] for i in range(len(lis2))}
# print(res)
def encription(message):
    message = message.lower()
    dic = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 
        'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
        's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}

    encrypting_message = " "
    for char in message:
        if char == " ":
            encrypting_message += "$"
        elif char.isalpha():
            encription = dic[char]
            encrypting_message += encription
        else:
            encrypting_message += char   
    return encrypting_message

    


