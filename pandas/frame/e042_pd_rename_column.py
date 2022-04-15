import pandas as pd
d = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
df=df.rename(columns = {'col2':'Column2'})
print("New DataFrame after renaming second column:")
print(df)
