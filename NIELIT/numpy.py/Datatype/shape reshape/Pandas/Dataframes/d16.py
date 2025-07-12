import pandas as pd
data={'Name':['Jai','Princi','Gaurav','Anuj'],'Age':[27,24,22,32],'Address':['Delhi','Kanpur','Allahabad','Kannauj'],'Qualification':["Msc","MA","MCA",'Phd']}
df=pd.DataFrame(data)
df["Name"]=df["Name"].str.lower()
print(df)