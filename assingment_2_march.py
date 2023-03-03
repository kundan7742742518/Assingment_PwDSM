# ANS = 1
"""
Matplotlib is a plotting library available for the Python programming language as a component of NumPy, 
a big data numerical handling resource.

It used becouse getting good insights from data through plot and plot give us batter undastending.
plot(x, y)
scatter(x, y)
bar(x, height)
hist(x, y)
step(x, y)
"""
# ANS = 2

"""
A scatter plot is a diagram where each value in the data set is represented by a dot.
"""
import numpy as np
import matplotlib.pyplot as plt 
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))
plt.scatter(x,y ,c = '#1324F0', alpha= 0.8)
plt.xlabel("This is my x-label")
plt.ylabel("This is my y-label")
plt.title("scatter plot")
plt.show()

# ANS - 3
"""
The subplot() function in Matplotlib is used to create multiple subplots in a single figure. 
It is particularly useful when we want to compare different plots side by side.
"""
x1 = np.array([0, 1, 2, 3, 4, 5]) 
y1 = np.array([0, 100, 200, 300, 400, 500])
x2 = np.array([0, 1, 2, 3, 4, 5]) 
y2 = np.array([50, 20, 40, 20, 60, 70])
x3 = np.array([0, 1, 2, 3, 4, 5])
y3 = np.array([10, 20, 30, 40, 50, 60])
x4= np.array([0, 1, 2, 3, 4, 5])
y4= np.array([200, 350, 250, 550, 450, 150])

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x1, y1)
plt.title('Line 1')

plt.subplot(2, 2, 2)
plt.plot(x2, y2)
plt.title('Line 2')

plt.subplot(2, 2, 3)
plt.plot(x3, y3)
plt.title('Line 3')

plt.subplot(2, 2, 4)
plt.plot(x4, y4)
plt.title('Line 4')

plt.show()


# ANS = 4
"""
It shows the relationship between a numeric and a categoric variable.
"""
import numpy as np
import matplotlib.pyplot as plt
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])
plt.bar(company,profit)
plt.xlabel("This are the FANG company")
plt.ylabel("This is the profit of FANG")
plt.title("company profit")
plt.show()

# ANS = 5
"""
A Box plot is a way to visualize the distribution of the data by using a box and some vertical lines.
It is known as the whisker plot
"""
import numpy as np
import matplotlib.pyplot as plt
box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
box = [box1 , box2]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
plt.boxplot(box)
plt.show()
