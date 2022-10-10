import pandas as pd

FILE_CSV='/home/christophe/Téléchargements/titanic.csv'
df = pd.read_csv(FILE_CSV)
print(df)

result = df.pivot_table(index=['sex'], values='who', aggfunc='count')
print(result)
result = df.pivot_table(index=['who'], values='sex', aggfunc='count')
print(result)
