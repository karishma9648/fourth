import pandas as pd
import numpy as np
df=pd.read_csv('iris.csv')
df = df.rename(columns={'sepal.width':'right.width'})
print(df)