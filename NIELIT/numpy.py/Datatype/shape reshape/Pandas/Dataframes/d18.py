import pandas as pd
data={'Name':['Jai','Princi','Gaurav','Anuj'],'Age':[27,24,22,32],'Address':['Delhi','Kanpur','Allahabad','Kannauj'],'Qualification':['Msc','MA','MCA','Phd']}
df=pd.DataFrame(data)
print(df)
df=["Age"]=df["Age"].replace(25,"Twenty five")
print(df)
