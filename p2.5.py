import matplotlib.pyplot as plt
Marks = [89,90,70,89,100,80,90,100,80,34]
Marks_Range=[10,20,30,40,50,60,70,80,90,100]
colors = 'r'
circle_area=25
contrast=0.9
plt.scatter(Marks,Marks_Range,s=circle_area,c=colors,alpha=contrast)
plt.title('Scatter plot-Marks')
plt.xlabel('Marks Obtained')
plt.show()