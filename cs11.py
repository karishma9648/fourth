import pandas as pd
import numpy as np
df=pd.read_csv('iris.csv')
column_sum = df['sepal.width'].sum()
print(column_sum)