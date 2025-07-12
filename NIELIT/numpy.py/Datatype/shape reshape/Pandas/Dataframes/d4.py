import pandas as pd
dict={'name':["aparna","panka","sudhir","Geeku"],'degree':["MBA","BCA","M.Tech",'MBA'],'score':[90,40,80,98]}
#creating a dataframe with booleanindex
df = pd.DataFrame(dict,index = [True,False,True,False])
#accessing