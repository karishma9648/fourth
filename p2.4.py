import numpy as np
import matplotlib.pyplot as plt
names=['group a','group b','group c']
values = [1,10,100]
plt.figure(figsize=(9,3))
plt.subplot(131)
plt.bar(names,values)
plt.subplot(132)
plt.scatter(names,values)
plt.subplot(133)
plt.plot(names,values)
plt.suptitle('Categorical Plotting')
plt.show()