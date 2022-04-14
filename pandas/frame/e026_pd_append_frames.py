import pandas as pd
import numpy as np
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print('After add one row:')
d2 = {'col1': 10, 'col2': 11, 'col3': 12}
df = df.append(d2, ignore_index=True)
print(df)

print('append (df,df2) w/ concat')
df = pd.DataFrame(data=d)
# w/ scalar, use index: https://stackoverflow.com/questions/17839973/constructing-pandas-dataframe-from-values-in-variables-gives-valueerror-if-usi
df2 = pd.DataFrame(data=d2, index=[0])
df = pd.concat([df, df2], ignore_index=True)
print(df)
