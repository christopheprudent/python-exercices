import pandas as pd

FILE_CSV='/home/christophe/Téléchargements/titanic.csv'
df = pd.read_csv(FILE_CSV)
print(df)

result = df.pivot_table('survived', index='class', columns='sex', aggfunc='count')
print(result, "\n")
result = df.pivot_table(index=['sex'], columns=['class'], values='survived', aggfunc='count')
print(result)
