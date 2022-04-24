import pandas as pd
s1 = pd.Series([0, 1, 2, 3], name='col1')
s2 = pd.Series([0, 1, 2, 3])
s3 = pd.Series([0, 1, 4, 5], name='col3')
print("Original Series:")
print(s1)
print("--------------------")
print(s2)
print("--------------------")
print(s3)
print("\nMerged Data (renaming columns):")
df = pd.concat([s1, s2, s3], axis=1, keys=['column1', 'column2', 'column3'])
print(df)