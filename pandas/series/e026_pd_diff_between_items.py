import pandas as pd
s = pd.Series([1, 3, 5, 8, 10, 11, 15])
print("Original Series:")
print(s)
print("\nDifference of differences between consecutive numbers of the said series:")
print(s.diff().tolist())
print(s.diff().diff().tolist())
print(s.diff().diff().diff().tolist())
