import pandas as pd

FILE_CSV='/home/christophe/Téléchargements/titanic.csv'

df = pd.read_csv(FILE_CSV)
print(df)

table = pd.pivot_table(df, index=["sex"], values="survived")
print(table)

result = df.pivot_table('survived', index='sex')
print(result)
result = df.groupby('sex')[['survived']].mean()
print(result)
