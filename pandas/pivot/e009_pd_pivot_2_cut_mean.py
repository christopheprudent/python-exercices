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

#result = df.pivot_table('survived', index=["sex", age], columns='class')
#result = df.pivot_table(values=['survived'], index=["sex", age], columns='class')
result = pd.pivot_table(df, values=['survived'], index=["sex", age], columns='class')
#result = pd.pivot_table(df[df.survived == 1], values=['survived'], index=["sex", age], columns='class')
print(result)

#df_count = df.groupby(["sex", age, 'class'])['survived'].apply(lambda x: (x==1).sum()).reset_index(name='count').agg({'count':'mean'})
df_count = df.groupby(["sex", age, 'class'])['survived'].apply(lambda x: (x==1).sum()).reset_index(name='count')
print(df_count)

print(df.groupby('sex')[['survived']].mean())
print(df.pivot_table('survived', ['sex', age], 'class'))
