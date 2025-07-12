import pandas as pd
import matplotlib.pyplot as plt
Student1={'Monthly':['Feb','Apr','June','Sep','Nov','Dec'],'Eng':[45,67,78,58,87,89],'Maths':[55,87,98,88,97,69]}
df1=pd.DataFrame(Student1)
df1['Total']= df1['Eng']+df1['Maths']
df1['PCT']=df1['Total']/2
plt.scatter('Monthly','PCT',s=50,color='r',data=df1)
plt.xlabel('Monthly EXam')
plt.ylabel('Percentage')
plt.title('Compare Percentage of Two Students')
plt.show()