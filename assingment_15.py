# ANS = 1
"""
Multiprocessing in Python is a built-in package that allows the system to run multiple processes simultaneously. 
It will enable the breaking of applications into smaller threads that can run independently.

It use ful becouse it will split the code bits and pices and run multiple micro processers. 
Becouse of this it will run very fast
"""
# ANS = 2
"""
By formal definition, multithreading refers to the ability of a processor to execute multiple threads concurrently, 
where each thread runs a process. 
Whereas multiprocessing refers to the ability of a system to run multiple processors concurrently, 
where each processor can run one or more threads.
"""

# ANS = 3
import multiprocessing
def square(num):
    print("squar:{}".format(num*num))
    
def cube(num):
    print("squar:{}".format(num*num*num))
if __name__ == '__main__':
    p1 = multiprocessing.Process(target= square , args=(10,))
    p2 = multiprocessing.Process(target= cube , args=(10,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
# This the one process that define multiprocess 

# ANS = 4
"""
Python multiprocessing Pool can be used for parallel execution of a function across multiple input values, 
distributing the input data across processes (data parallelism).
Use the multiprocessing. 
Pool class when you need to execute tasks that may or may not take arguments 
and may or may not return a result once the tasks are complete. Use the multiprocessing. 
Pool class when you need to execute different types of ad hoc tasks, 
such as calling different target task functions
"""

# ANS = 5

"""
Create the Process Pool.
Submit Tasks to the Process Pool.
Wait for Tasks to Complete (Optional)
Shutdown the Process Pool.
"""
# ANS = 6
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
        
from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
    
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])

    
    