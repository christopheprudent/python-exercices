import pandas as pd

FILE_CSV='/home/christophe/Téléchargements/titanic.csv'
df = pd.read_csv(FILE_CSV)
print(df)

result = df.groupby(['sex', 'class'])['survived'].aggregate('mean')
print(result)
result = df.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack()
print(result)
