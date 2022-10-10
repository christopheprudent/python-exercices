"""
check missing values of children
"""

import pandas as pd
import numpy as np

FILE_CSV='/home/christophe/Téléchargements/titanic.csv'
df = pd.read_csv(FILE_CSV)
print(df)

result = df.loc[df['who']=='child'].isnull().sum()
print(result)
