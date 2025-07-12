import pandas as pd
dict={'name':["aparna","panka","sudhir","Geeku"],'degree':["MBA","BCA","M.Tech",'MBA'],'score':[90,40,80,98]}
#creating a dataframe 
df = pd.DataFrame(dict)
for i in df.itertuples():
    print(i)