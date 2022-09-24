import pandas as pd

FILE_CSV='/home/christophe/Téléchargements/titanic.csv'
df = pd.read_csv(FILE_CSV)
print(df)

#result = df.pivot_table(index=['sex'], columns=['pclass'], aggfunc='count')
result = df.pivot_table(index=['sex'], values=['who'], columns=['pclass'], aggfunc='count')
print(result)
