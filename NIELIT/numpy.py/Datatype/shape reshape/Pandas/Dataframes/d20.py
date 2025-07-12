import pandas as pd
data={'Name':['Jai','Princi','Gaurav','Anuj'],'Age':[27,24,22,32],'Address':["Nagpur junction",'Kanpur junction','Nagpur junction','Kannauj junction'],'Qualification':['Msc','MA','MCA','Phd']}
df=pd.DataFrame(data)
new=df["Address"].replace()
df["Name"]=df["Name"].str.cat(new,sep=",")
print(df)