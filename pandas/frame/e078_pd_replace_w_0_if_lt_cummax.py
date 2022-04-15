import pandas as pd
df=pd.DataFrame({'rnum':[23, 21, 27, 22, 34, 33, 34, 31, 25, 22, 34, 19, 31, 32, 19]})
print("Original DataFrame:")
print(df)
print(df.cummax())
df['rnum']=df.rnum.where(df.rnum.eq(df.rnum.cummax()),0)
print("\nReplace current value in a dataframe column based on last largest value:")
print(df)
