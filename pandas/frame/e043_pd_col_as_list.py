import pandas as pd
d = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
col2_list = df["col2"].tolist()
print("Col2 of the DataFrame to list:")
print(col2_list)
