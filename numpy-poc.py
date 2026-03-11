import numpy as np
import sys
import time

arr = np.array([1,2,3])
print(arr[0])

l = range(1000)
print(sys.getsizeof(5)*len(l))

a = np.arange(1000)
print(a.size*a.itemsize)

SIZE = 100000
l1 = range(SIZE)
l2 = range(SIZE)

#python list
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("list took", (time.time() - start)*1000)

# numpy array
a1 = np.arange(SIZE)
a2 = np.arange(SIZE)
start = time.time()
result = a1+a2
print("numpy array took", (time.time() - start)*1000)