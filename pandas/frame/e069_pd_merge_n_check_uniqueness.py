import pandas as pd
df = pd.DataFrame({
    'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'Age': [18.5, 21.2, 22.5, 22, 23]
})
print("Original DataFrame:")
print(df)

df1 = df.copy(deep = True)
df = df.drop([0, 1])
df1 = df1.drop([2])
print("\nNew DataFrames:")
print('left: w/ rows [0, 1] dropped')
print(df)
print('right: w/ rows [2] dropped')
print(df1)

print('\n"one_to_one” or "1:1": check if merge keys are unique in both left and right datasets:"')
df_one_to_one = pd.merge(df, df1, validate = "one_to_one")
print(df_one_to_one)
print('\n"one_to_many” or “1:m”: check if merge keys are unique in left dataset:')
df_one_to_many = pd.merge(df, df1, validate = "one_to_many")
print(df_one_to_many)
print('“many_to_one” or “m:1”: check if merge keys are unique in right dataset:')
df_many_to_one = pd.merge(df, df1, validate = "many_to_one")
print(df_many_to_one)
