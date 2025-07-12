import pandas as pd
d={'Name':['tom','jack','steve','ricky'],'Age':[28,34,29,42]}
df=pd.DataFrame(d,index=['e1','e2','e3','e4'])
print('our dataframe is')
print(df)

#droping values
df.drop(['e1','e4'],inplace=True)
print(df)