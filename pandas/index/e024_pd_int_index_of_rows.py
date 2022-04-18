import pandas as pd
import numpy as np
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, None, 33, 30, 31, None]},
     index = ['t1', 't2', 't3', 't4', 't5', 't6'])
print("Original DataFrame:")
print(df)
index = df['weight'].index[df['weight'].apply(np.isnan)]
df_index = df.index.values.tolist()
print("\nInteger index of rows with missing data in 'weight' column of the said dataframe:")
print([df_index.index(i) for i in index])
'''
df['weight']
t1    35.0
t2     NaN
t3    33.0
t4    30.0
t5    31.0
t6     NaN
Name: weight, dtype: float64
df['weight'].index
Index(['t1', 't2', 't3', 't4', 't5', 't6'], dtype='object')
df['weight'].apply(np.isnan)
t1    False
t2     True
t3    False
t4    False
t5    False
t6     True
Name: weight, dtype: bool
df['weight'].index[df['weight'].apply(np.isnan)]
Index(['t2', 't6'], dtype='object')
df['weight'].index[df['weight'].apply(np.isnan)].values
array(['t2', 't6'], dtype=object)
df['weight'].index[df['weight'].apply(np.isnan)].values.tolist()
['t2', 't6']
ix = df['weight'].index[df['weight'].apply(np.isnan)]
Index(['t2', 't6'], dtype='object')
df.index.values.tolist()
['t1', 't2', 't3', 't4', 't5', 't6']
[df_index.index(i) for i in ix]
[1, 5]
df_index.index('t1')
0
df_index.index('t2')
1
'''
