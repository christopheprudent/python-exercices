"""
find the probability of survival by class, gender, solo boarding and port of embarkation
"""

import pandas as pd

FILE_CSV='/home/christophe/Téléchargements/titanic.csv'
df = pd.read_csv(FILE_CSV)
print(df)

result = df.pivot_table(index=['class', 'sex', 'alone', 'embark_town'], values='survived', aggfunc='mean')
print(result)
result = df.pivot_table(values='survived', index=['sex' , 'alone'], columns=['embark_town', 'class'])
print(result)
