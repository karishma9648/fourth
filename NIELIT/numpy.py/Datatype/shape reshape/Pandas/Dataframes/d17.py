import pandas as pd
data={'Name':['Jai','Princi','Gaurav','Anuj'],'Age':[27,24,22,32],'Address':['Delhi','Kanpur','Allahabad','Kannauj'],'Qualification':['Msc','MA','MCA','Phd']}
df=pd.DataFrame(data)
df.dropna(inplace = True)
df["Address"]=df["Address"].str.split("a")
print(df)