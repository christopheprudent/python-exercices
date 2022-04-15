import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
if 'col4' in df.columns:
  print("Col4 is present in DataFrame.")
else:
  print("Col4 is not present in DataFrame.")
if 'col1' in df.columns:
  print("Col1 is present in DataFrame.")
else:
  print("Col1 is not present in DataFrame.")
