import numpy as np
a=np.array( [ [1,2,3], [4,5,6], [11,12,13], [14,15,16] ] )
c=np.array_split( a,  2)
print('Array Split into 2 part')
print(c)
c=np.array_split( a, 3,  axis=0)
print('Array Split at Axis=0')
print(c)
c=np.array_split( a, 3,  axis=1)
print('Array Split at Axis=1')
print(c)

