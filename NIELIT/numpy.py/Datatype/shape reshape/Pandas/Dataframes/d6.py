import pandas as pd
dict={'name':["aparna","panka","sudhir","Geeku"],'degree':["MBA","BCA","M.Tech",'MBA'],'score':[90,40,80,98]}
#creating a dataframe 
df = pd.DataFrame(dict)
#using a comparison operator for filtering of data
row=df['degree']=='BCA'
print(row)
print(df[row])