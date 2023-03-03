# ANS = 1
"""
The ability of a processor to execute multiple threads simultaneously.
Python multithreading facilitates sharing data space and resources of multiple threads with the main thread. 
It allows efficient and easy communication between the threads
import threading 
"""
# ANS = 2
"""
The threading module provided with Python includes 
a simple-to-implement locking mechanism that allows you to synchronize threads.

activeCount() - Returns the number of thread objects that are active.
currentThread() - Returns the number of thread objects in the caller's thread control. 
enumerate() - Returns a list of all thread objects that are currently active.
""" 
# ANS = 3

"""
run()- method invokes the callable object passed to the object's constructor as the target argument
start()- method is an inbuilt method of the Thread class of the threading module in Python. 
It is used to start a thread's activity
join()- method takes all items in an iterable and joins them into one string
is_alive()- method is an inbuilt method of the Thread class of the threading module in Python
"""

# ANS = 4
import threading

def squir(x):
    squares = []
    for i in range(x):
        a = i*i
        squares.append(a)
    print(squares)           
def cube(x):
    cubes  = []
    for i in range(x):
        a = i*i*i
        cubes.append(a)
    print(cubes)           

thred = threading.Thread (target= squir , args= (10,))
thred1 = threading.Thread (target = cube , args=(10,))
thred.start()
thred1.start()
thred.join()
thred1.join()
print("Well done")

# ANS = 5
"""
This model provides more concurrency than the many-to-one model. 
It also allows another thread to run when a thread makes a blocking system call. 
It supports multiple threads to execute in parallel on microprocessors. 
Disadvantage of this model is that creating user thread requires the corresponding Kernel thread.
"""
# ANS  = 6

"""
deadlock:-Two threads hold locks on different resources, each waiting indefinitely for the other to release its lock. 
race condition:- Two (or more) threads alter the state of a shared resource concurrently, 
leaving it in an unpredictable state
"""