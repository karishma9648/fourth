import pandas as pd
import numpy as np
df=pd.read_csv('iris.csv')
df['new_column'] = df ['column1']+df['column']