import numpy as np
a = np.array([ 1,4,3,2,5,8,7,6]) 
print('Values of Array - A ')
print(a)
print('Sorted Array: ')
print(np.sort(a))
print('Search the Even Numbers')
x=np.where(a%2==0)
print(x)

# t = np.array([ [10,20,30,'red'],
#                 [21,31,41,'green'],
#                 [50,60,70,'brown'],
#                 [89,97,11,'green']  ])
# row= np.where(t == 'green')
# print(row)
# rs= t[row]
# print(rs)