import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32]},
     index = ['t1', 't2', 't3', 't4', 't5', 't6'])
print("Original DataFrame:")
print(df)
print("\nSet school code 's004' to 's005' (with 't6' index):")
df.at['t6', 'school_code'] = 's005'
print(df)
print("\nSet date_of_birth of 'Alberto Franco' to '16/05/2002' (with 't1' index):")
df.at['t1', 'date_of_birth'] = '16/05/2002'
print(df)
