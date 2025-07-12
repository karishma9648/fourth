#importing pandas as pd
import pandas as pd 
#importing numpy as np
import numpy as np
#dictionary of lists
dict = {'First Score':[100,90,np.nan,95],'Second Score':[30,45,56,np.nan],'Third Score':[np.nan,40,80,98]}
#creating a dataframe using dictionary 
df = pd.DataFrame(dict)
#filling missing value usingfillna
df.fillna(0)