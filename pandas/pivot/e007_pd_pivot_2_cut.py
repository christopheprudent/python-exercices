import pandas as pd
FILE_CSV='/home/christophe/Téléchargements/titanic.csv'
df = pd.read_csv(FILE_CSV)

df['age cut'] = pd.cut(df['age'], [0, 10, 30, 60, 80])
print(df)

# by cut of ages
result = pd.pivot_table(df, index=["survived"], values=["age cut"], aggfunc=[len])
print(result)
_counts = df.groupby('age cut').size()
print(_counts)
