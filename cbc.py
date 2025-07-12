import numpy as np
import matplotlib.pyplot as plt
 # data to plot
n_groups = 4
Sales_Voltas = (90, 55, 40, 65)
Sales_Samsung = (85, 62, 54, 20)
Year_Sales= ('2016', '2017', '2018', '2020')
34
 # create plot
y_pos= np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
rects1 = plt.bar(y_pos , Sales_Voltas , bar_width, alpha=opacity, color='b', label='Voltas')
rects2 = plt.bar(y_pos + bar_width, Sales_Samsung ,  bar_width, alpha=opacity, color='g', label='Samsung')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Scores')
plt.xticks(y_pos + bar_width,  Year_Sales)
plt.legend()
plt.show()
 