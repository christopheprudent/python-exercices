import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)

# df['col1'].where(df['col1'] == df['col1'].max())
print("Row where col1 has maximum value:")
print(df['col1'].argmax())
print("Row where col2 has maximum value:")
print(df['col2'].argmax())
print("Row where col3 has maximum value:")
print(df['col3'].argmax())
