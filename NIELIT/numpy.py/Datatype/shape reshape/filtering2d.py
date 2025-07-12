import numpy as np
a = np.array([ [1,5,2,5], [5,7,6,5] ]) 
print('Filtering the Value')
filter=(a%2==0)
print(filter)
x=a[filter]
print(x)
t = np.array([[10,20,30,'red'],
 [21,31,41,'green'],
 [50,60,70,'brown'],
 [89,97,11,'green']])
filter=(t == 'green')
print(filter)
x=t[filter]
print(x)