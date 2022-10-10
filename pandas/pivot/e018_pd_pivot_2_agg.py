"""
separate the gender according to whether they traveled alone or not to get the probability of survival
"""

import pandas as pd

FILE_CSV='/home/christophe/Téléchargements/titanic.csv'
df = pd.read_csv(FILE_CSV)
print(df)

result = df.pivot_table(index=['sex', 'alone'], columns=['class'], values='survived', aggfunc='mean')
print(result)
