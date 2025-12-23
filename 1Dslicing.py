import numpy as np
#1d array
array=np.array([10,20,30,40,50])
print(array)
#indexing
print("first element:",array[0])
print("last element:",array[-1])
#slicing
print("array:",array[:])
print("last 3 elemnts:",array[2:])
print("first 3 elements:",array[:3])
print("elements from 1 to end:",array[0:])
#basic operations
print("sum of elements:",array.sum())
print("average of elements:",array.mean())
