import pandas as pd
FILE_CSV='/home/christophe/Téléchargements/titanic.csv'
df = pd.read_csv(FILE_CSV)

age = pd.cut(df['age'], [0, 10, 30, 60, 80])
print(df)

# pclass            1   2    3
# sex    age                  
# female (0, 10]    1   8   22
#        (10, 30]  34  36   57
#        (30, 60]  48  30   22
#        (60, 80]   2   0    1
# male   (0, 10]    2   9   22
#        (10, 30]  24  43  151
#        (30, 60]  63  44   76
#        (60, 80]  12   3    4

#result = df.pivot_table('survived', index=["sex", age], columns='pclass', aggfunc='count')
#result = df.pivot_table(values=['survived'], index=["sex", age], columns='pclass', aggfunc='count')
#result = pd.pivot_table(df, values=['survived'], index=["sex", age], columns='pclass', aggfunc='count')
result = pd.pivot_table(df[df.survived == 1], values=['survived'], index=["sex", age], columns='pclass', aggfunc='count')
print(result)

#print(df[(df.age <= 10) & (df.sex == 'male') & (df.pclass == 1)])
print(df[(df.age <= 10) & (df.pclass == 1)])
