import pandas as pd
d={'Name':['tom','jack','steve','ricky'],'Age':[28,34,29,42]}
df=pd.DataFrame(d,index=['e1','e2','e3','e4'])
print('our dataframe is')
print(df)

#simply concatenate both dataframe
new_row=pd.DataFrame({'Name':'Ajay','Age':33},index=[0])
df=pd.concat([new_row, df])
print(df)
df=pd.concat([new_row, df]).reset_index(drop= True)
print(df)
df=pd.concat([new_row, df]).reset_index(drop= False)
print(df)