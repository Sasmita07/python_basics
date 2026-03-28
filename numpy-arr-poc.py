import numpy as np

arr = np.array([[1,2],[3,4],[5,6]])
# ndim is an attribute used primarily with the NumPy library to retrieve the number of dimensions (axes) of an array object. It returns an integer
print(arr.ndim)
print(arr.itemsize)
print(arr.dtype)

# create float type array
arr = np.array([[1,2],[3,4],[5,6]], dtype = np.float64)
print(arr.dtype)
print(arr.size)

# create complex type array
arr = np.array([[1,2],[3,4],[5,6]], dtype = complex)
print(arr)

zeros_arr = np.zeros((3,3))
print(zeros_arr)

ones_arr = np.ones((3,3))
print("Ones arr:", ones_arr)

range_arr = np.arange(1,5)
print("Range arr:", range_arr)

# step of 2
range_step_arr = np.arange(1,5,2)
print("Range step arr:", range_step_arr)

linspace_arr = np.linspace(1,5,10)
print("line space arr:", linspace_arr)

arr = np.array([[1,2],[3,4],[5,6]])
reshape_arr = arr.reshape(2,3)
print("reshape_arr 1:", reshape_arr)
reshape_arr = arr.reshape(6,1)
print("reshape_arr 2:", reshape_arr)
ravel_arr = arr.ravel()
print("ravel the array:", ravel_arr)

print("The array min:", arr.min())
print("The array max:", arr.max())
print("The array sum:", arr.sum())
print("The array axis col sum:", arr.sum(axis=0))
print("The array axis row sum:", arr.sum(axis=1))

print("The array sqaureroot:", np.sqrt(arr))
print("The array std:", np.std(arr))

arr1 = np.array([[1,1],[0,1]])

arr2 = np.array([[1,2],[3,4]])
print(arr1 + arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1.dot(arr2))


# indexing
print("The array indexing:", arr[0:2])
arr3 = np.array([[1,2,3],[3,4,5],[5,6,7]])
print("The array indexing getting second element:", arr3[0:2,2])
print("The array reverse indexing:", arr[-1])


# iterating the array
for row in arr3:
    print(row)

for cell in arr3.flat:
    print(cell)

a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)
c = np.vstack((a,b))
print("vstack arr:", c)
d = np.hstack((a,b))
print("hstack arr:", d)

result = np.hsplit(np.arange(30).reshape(2,15),3)
result1 = np.vsplit(np.arange(30).reshape(2,15),2)
print("hsplit arr:", result[0])
print("vsplit arr:", result1[0])

temparr = np.arange(12).reshape(3,4)
boolarr = temparr > 4
print("boolean arr:", temparr[boolarr])
temparr[boolarr] = -1
print("boolean arr reassign:", temparr[boolarr])