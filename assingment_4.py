# ANS = 1
lis = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
lis.sort(key = lambda x : x[1]) 
print(lis)

# ANS = 2
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda n : n**2 ,x)))

# ANS = 3
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tuple(map(lambda n : str(n) ,x)))
# ANS  = 4
from functools import reduce
num =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,25]
ans = reduce(lambda x, y: x * y, num)
print(ans)

# ANS = 5
num = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
ku = filter(lambda x : x%2 == 0 and x%3 == 0, num)
print(list(ku)) 

# ANS = 6
num = ['python', 'php', 'aba', 'radar', 'level']
ant = filter(lambda x : (x == "".join(x[::-1])),num)
print(list(ant))





