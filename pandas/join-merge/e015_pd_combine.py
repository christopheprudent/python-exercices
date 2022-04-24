import pandas as pd
df1 = pd.DataFrame({'A': [None, 0, None], 'B': [3, 4, 5]})
df2 = pd.DataFrame({'A': [1, 1, 3], 'B': [3, None, 3]})

print("Original DataFrames:")
print(df1)
print("--------------------")
print(df2)

print("\nMerge two dataframes (replacing null w/ non-null):")
result = df1.combine_first(df2)
print(result)
