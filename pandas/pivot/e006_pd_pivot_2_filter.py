import pandas as pd

FILE_CSV='/home/christophe/Téléchargements/titanic.csv'

df = pd.read_csv(FILE_CSV)
print(df)

table = pd.pivot_table(df, index=["sex", "age", "class"], values="survived")
print(table)

result = df.pivot_table('survived', index=['sex', 'age'], columns='class')
print(result)
