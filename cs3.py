import pandas as pd
import numpy as np
df=pd.read_csv('iris.csv')
filter_df = df[df['']>10]
print(filter_df)