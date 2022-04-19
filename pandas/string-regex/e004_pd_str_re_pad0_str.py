import pandas as pd
nums = {'amount': ['10', '250', '3000', '40000', '500000']}
print("Original dataframe:")
df = pd.DataFrame(nums)
print(df)

print("\nAdd leading zeros:")
df['amount-pad0-zfill'] = list(map(lambda x: x.zfill(8), df['amount']))
df['amount-pad0-rjust'] = df['amount'].str.rjust(8, '0')
print(df)
