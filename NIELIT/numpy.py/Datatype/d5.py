import numpy as np 
a=np.array([1.1,2.5,0.6,4.7,5.3])
print('values of array-A')
print(a)
print('Base of Array-A:',a.base)
b=a.copy()
b[0]=10;
print('Values of Array-A')
print(b)
print('Base of Array-B:',b.base)

c=a.view()
c[0]=10;
print('Values of Array-A')
print(c)
print('Base of Array-C:',c.base)