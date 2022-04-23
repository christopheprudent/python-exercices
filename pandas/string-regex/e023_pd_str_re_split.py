import pandas as pd
df = pd.DataFrame({
    'name': ['Alberto  Franco','Gino Ann Mcneill','Ryan  Parkes', 'Eesha Artur Hinton', 'Syed  Wharton'],
    'date_of_birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})
print("Original DataFrame:")
print(df)

'''
Expand the split strings into separate columns.

If True, return DataFrame/MultiIndex expanding dimensionality.
If False, return Series/Index, containing lists of strings
'''
df[["first", "middle", "last"]] = df["name"].str.split(" ", expand = True)
print("\nNew DataFrame (after splitting column 'name'):")
print(df)
