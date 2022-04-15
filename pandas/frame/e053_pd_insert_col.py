import pandas as pd
d = {'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
new_col = [1, 2, 3, 4, 7]  
# insert the said column at the beginning in the DataFrame
idx = 0
df.insert(loc=idx, column='col1', value=new_col)
print("\nNew DataFrame")
print(df)
