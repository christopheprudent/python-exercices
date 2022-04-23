import pandas as pd
import re as re
#pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'name_email': ['Alberto Franco af@gmail.com','Gino Mcneill gm@yahoo.com','Ryan Parkes rp@abc.io', 'Eesha Hinton', 'Gino Mcneill gm@github.com']
    })
print("Original DataFrame:")
print(df)

def find_email(text):
    email = re.findall(r'[\w\.-]+@[\w\.-]+',str(text))
    return ",".join(email)

df['email']=df['name_email'].apply(lambda x: find_email(x))
print("\nExtracting email from dataframe columns:")
print(df)
