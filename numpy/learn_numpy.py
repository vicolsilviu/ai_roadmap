import numpy as np
import timeit


array = np.arange(10)
array=np.array([1,2,3,5,6,7,8,9])
# print(array)
# print(array.shape)

np1=np.arange(0,30,3)
# print(np1)

np2=np.zeros((2,10))
# print(np2)

np3= np.full((2,10),6)
# print(np3)
# print(np3[0,0])
array = np.arange(10)
# print(array[2:5])
# print(array[:2])
# print(array[2:])
# print(array[-3:-1])
# print(array[::2])
# print(array[::-1])

np2=np.array([[1,2,3],[4,5,6]])
# print(np2)
# print(np2.shape)

# Numpy universal functions
np1=np.array([1,2,3,-4,5,6,7,8,9])
# print(np.sqrt(np1))
# Absolute value
# print(np.absolute(np1))
# print(np.exp(np1))
# print(np.min(np1))
# print(np.max(np1))
# print(np.mean(np1))
# print(np.median(np1))
# print(np.std(np1))
# print(np.var(np1))
# print(np.sum(np1))
# print(np.sign(np1))
array = np.arange(10)
np2=array.view()
# array=np.array([[1,2,3],[4,5,6]])
# print(np2)
# array[0]=100
# print(array)
# print(np2)
# print(array.shape)
np4=np1.reshape(3,3)
# print(np1.reshape(3,3))
# print(np4.reshape(-1))
# array = np.arange(10)
# for x in np4:
#     for y in x:
#         print(y)
# np3=np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
# print(np3.shape)
# for x in np.nditer(np3):
#     print(x)
# np1=np.array([1,2,3,-4,5,6,7,8,9])
# print(np1.sort())
# # print(np1)
# # Return a copy, not change the original array
# print(np1.sort())
# print(np1)
np1=np.array([1,2,3,-4,5,6,7,8,9])
# x = np.where(np1>5)
# print(x)
# print(np1[x])
x = np.where(np1==5)
# print(x)
# print(x[0])
# Return odd items
# z=np.where(np1%2==1)
# print(np1)
# print(z[0])
filtered=np1%2==0
# print(np1[filtered])
# print(np1[np1%2==0])
# print(np1[(np1>2)& (np1<5)])

random_array2=np.random.random((5,5))
# print(random_array2)
a=np.array([[1,2,3,4,5],[1,2,3,4,5]])
b=np.array([[6,7,8,9,10],[6,7,8,9,10]])
# print(a*b)
# print(np.square(1))
# print(np.sum(a))
# print(np.sum(b))

a = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])

# # Define the function to time
# def sum_array():
#     np.sum(a)

# # Use timeit to measure the execution time
# execution_time = timeit.timeit(sum_array, number=1000)  # Adjust number for more or fewer repetitions

# print(f"Average execution time: {execution_time / 1000:.6f} seconds")

# print(np.std(a))
# print(np.var(a))
# eye = np.eye(4)
# print(eye)
# linspace = np.linspace(0, 10, 5)
# print(linspace)
# arange = np.arange(0, 10, 2)
# # print(arange)

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# # Vertical stack
# vstacked = np.vstack((a, b))

# # Horizontal stack
# hstacked = np.hstack((a, b))

