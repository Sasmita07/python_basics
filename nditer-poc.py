import numpy as np

a = np.arange(12).reshape(3,4)

for cell in a.flatten():
    print(cell)

for ele in np.nditer(a, order='C'):
    print(ele)
print("---------------")
for ele in np.nditer(a, order='F'):
    print(ele)

print("---------------")
for ele in np.nditer(a, order='F',flags=['external_loop']):
    print(ele)

print("---------------")
for ele in np.nditer(a, op_flags=['readwrite']):
    ele[...] = ele * ele
    print(ele)
print("---------------")
b = np.arange(3,15,4).reshape(3,1)

# shape of the arrays should be compatiable
for x,y in np.nditer([a,b]):
    print(x,y)