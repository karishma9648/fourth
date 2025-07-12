import numpy as np 
a=np.array([1.1,2.5,0.6,4.7,5.3])
print('values of array')
print(a)
print('Data Type of Array:',a.dtype)

a=a.astype("i")
print("Values of array")
print(a)
print('Data Type of Array:',a.dtype)

a=a.astype(bool)
print("Values of array")
print(a)
print('Data Type of Array:',a.dtype)
