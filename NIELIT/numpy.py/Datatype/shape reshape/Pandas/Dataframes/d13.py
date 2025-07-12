#importing pandas as pd
import pandas as pd 
#importing numpy as np
import numpy as np
#dictionary of lists
dict = {'First Score':[100,np.nan,np.nan,95],'Second Score':[30,np.nan,45,56],'Third Score':[52,np.nan,80,98],'Fourth Score':[60,67,68,65]}
#creating a dataframe using dictionary 
df = pd.DataFrame(dict)
#using dropna() function
print(df.dropna(axis=1))