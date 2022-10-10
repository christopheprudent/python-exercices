import pandas as pd

FILE_CSV='/home/christophe/Téléchargements/titanic.csv'
df = pd.read_csv(FILE_CSV)
print(df)

result = df.pivot_table('survived', index='sex', columns='class', margins=True)
print(result)
