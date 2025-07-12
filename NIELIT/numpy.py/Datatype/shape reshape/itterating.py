import numpy as np
a = np.array([ [1, 2, 3, 4],[5, 6, 7, 8]])
print('Simple Loop - Print Rows')
for row in a:
 print(row)
print('Simple Loop - Print each value')    
for row in a:
 for col in row:
  print(col)
 print('nditer( ) - Print each value') 
for val in np.nditer(a):
 print(val)
 print('ndenumerate( ) - Print (id ,value)') 
for id,val in np.ndenumerate(a):
 print(id,val)

 
 