import pandas as pd
import re

# find occurs of sub in s
def occurs(s, sub):
    return [(m.start(0), m.end(0)) for m in re.finditer(sub, s)]

df = pd.DataFrame({
    'name_code': ['c0001','1000c','b00c2', 'b2c02', 'c2222'],
    'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})
print("Original DataFrame:")
print(df)
print("\nIndex (start, end) of substring '2' in a 'name_code' column :")
df['Index'] = list(map(lambda x: occurs(x, '2'), df['name_code']))
print(df)

