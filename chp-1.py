class Myclass:
    common = 10
    def __init__ (self):
        self.myvariable = 3
    def myfunction (self, arg1, arg2):
        return self.myvariable

instance = Myclass()
print("instance.myfunction(1, 2)" , instance.myfunction(1, 2))

instance2 = Myclass()
print("instance.common ",instance.common)
print("instance2.common ",instance2.common)

Myclass.common = 30

print("instance.common ", instance.common)

print("instance2.common ", instance2.common)

instance.common = 10
print("instance.common ", instance.common)

print("instance2.common " , instance2.common)
Myclass.common = 50

print("instance.common ", instance.common)
print("instance2.common " , instance2.common)

class AnotherClass (Myclass):
    # The "self" argument is passed automatically
    # and refers to the class's instance, so you can set
    # instance variables as above, but from within the class.
    def __init__ (self, arg1):
        self.myvariable = 3
        print (arg1)

instance = AnotherClass ("hello")
print("instance.myfunction (1, 2) " , instance.myfunction (1, 2))

instance.test = 10
print("instance.test " , instance.test)

------------------------------------------------------------------------------

# In this program, 
# we check if the number is positive or
# negative or zero and 
# display an appropriate message

num = 1

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")



# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 6, 3, 8, -3, 2, 5, 44, 12]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)
------------------------------------------------------

import random

def do_something(count,out_list):
	for i in range(count):
		out_list.append(random.random())
----------------------------------------------------------
f = open ('test.txt', 'w')
f.write ('first line of file \n') 

f.write ('second line of file \n') 

f.close()
f = open ('test.txt')
content = f.read()
print (content)

f.close()
---------------------------------

# IF

# In this program, we check if the number is positive or negative or zero and 
# display an appropriate message

num = 1
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# FOR
# Program to find the sum of all numbers stored in a list
numbers = [6, 6, 3, 8, -3, 2, 5, 44, 12]
sum = 0
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)


#WHILE
# Program to add natural numbers upto sum = 1+2+3+...+n

n = 10
# initialize sum and counter
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
--------------------------------------------

example = [1, ["another", "list"], ("a", "tuple")]
example
mylist = ["element 1", 2, 3.14]
mylist
mylist[0] = "yet element 1"
print(mylist[0])
mylist[-1] = 3.15
print (mylist[-1])
mydict = {"Key 1": "value 1", 2: 3, "pi": 3.14}
print(mydict)
mydict["pi"] = 3.15
print(mydict["pi"])
mytuple = (1, 2, 3)
print(mytuple)
myfunc = len
print (myfunc(mylist))
----------------------------------------------

from do_something import *
import time
import multiprocessing


if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   
    procs = 10   
    jobs = []
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process\
                  (target=do_something,args=(size,out_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print ("List processing complete.")
    end_time = time.time()
    print("multiprocesses time=", end_time - start_time)
----------------------------------------------------------

from do_something import *
import time
import threading

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000
    threads = 10  
    jobs = []
    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(target=do_something(size, out_list))
        jobs.append(thread)
    for j in jobs:
        j.start()

    
    for j in jobs:
        j.join()

    print ("List processing complete.")
    end_time = time.time()
    print("multithreading time=", end_time - start_time)
	
-------------------------------------------------------------
import time
from do_something import *

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   
    n_exec = 10
    for i in range(0, n_exec):
        out_list = list()
        do_something(size, out_list)
       
 
    print ("List processing complete.")
    end_time = time.time()
    print("serial time=", end_time - start_time)
    ---------------------------------------------------------
    import time
from do_something import *

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   
    n_exec = 10
    for i in range(0, n_exec):
        out_list = list()
        do_something(size, out_list)
       
 
    print ("List processing complete.")
    end_time = time.time()
    print("serial time=", end_time - start_time)
    ------------------------------------------------
    import time
from do_something import *

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   
    n_exec = 10
    for i in range(0, n_exec):
        out_list = list()
        do_something(size, out_list)
       
 
    print ("List processing complete.")
    end_time = time.time()
    print("serial time=", end_time - start_time)
    