import pandas as pd
df = pd.DataFrame({'W':[68,75,86,80,66],'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
print("Original DataFrame")
print(df)

print("\nReverse column order:")
print(df.loc[:, ::-1])
print("\nReverse row order:")
print(df.loc[::-1])
print("\nReverse row order and reset index:")
print(df.loc[::-1].reset_index(drop = True))
