import pandas as pd 
from datetime import datetime 
import numpy as np 
range_date = pd.date_range(start='01/01/2019',end='01/08/2019',freq='min')
df=pd.DataFrame(range_date,columns=['data'])
df['date']= np.random.randint(0,100,size=len(range_date))
string_data =[str(x)for x in range_date]
print(string_data[1:11])
