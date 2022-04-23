import pandas as pd
import re as re
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['7277 Surrey Ave.1111','920 N. Bishop Ave.','9910 Golden Star St.', '1025 Dunbar St.', '1700 West Livingston Court']
    })
print("Original DataFrame:")
print(df)
def find_gt_940(text):
    '''
    result = re.findall(r'94[1-9]|9[5-9]\d|[1-9]\d{3,}',text)
    return " ".join(result)
    '''
    lnums = re.findall("\d+",text)
    result = []
    for n in lnums:
        if int(n) > 940:
            result.append(n)
    return " ".join(result)
df['num_gt_940']=df['address'].apply(lambda x: find_gt_940(x))
print("\nExtracting numbers (if gt 940) from 'address' column:")
print(df)
