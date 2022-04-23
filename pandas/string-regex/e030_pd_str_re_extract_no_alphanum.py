import pandas as pd
import re as re
df = pd.DataFrame({
    'company_code': ['c0001#','c00@0^2','$c0003', 'c0003', '&c0004'],
    'year': ['year 1800','year 1700','year 2300', 'year 1900', 'year 2200']
    })
print("Original DataFrame:")
print(df)
def find_nonalpha(text):
    #result = re.findall("[^A-Za-z0-9 ]",text)
    result = re.findall("\W",text)
    return result
df['nonalpha']=df['company_code'].apply(lambda x: find_nonalpha(x))
print("\nExtracting only non alphanumeric characters from company_code:")
print(df)
