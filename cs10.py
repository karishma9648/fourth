import pandas as pd
import numpy as np
df=pd.read_csv('iris.csv')
statistics = df.describe()
print(statistics)