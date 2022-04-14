import pandas as pd
import numpy as np

exam_data  = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print(df)

print('\ninfo DataFrame')
print(df.info())

print('\nmode ligne, id=c')
print(df.loc['c'])
print('3 premières lignes')
print(df.iloc[:3])

print('\nsélection de colonnes')
print(df[['name', 'score']])
print('\nsélection de lignes et de colonnes')
print(df.iloc[[1, 3, 6], [1, 3]])
