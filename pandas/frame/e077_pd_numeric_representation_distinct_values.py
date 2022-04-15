import pandas as pd
df = pd.DataFrame({
    'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill'],
    'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'Age': [18.5, 21.2, 22.5, 22, 23]
})
print("Original DataFrame:")
print(df)
label1, unique1 = pd.factorize(df['Name'])
print("\nNumeric representation of an array by identifying distinct values:")
print(label1)
print(unique1)
