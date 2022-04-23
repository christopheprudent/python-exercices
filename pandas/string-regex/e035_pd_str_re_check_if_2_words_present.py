import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['99100 Surrey Ave.','92 N. Bishop Ave.','9910 Golden Star Ave.', '102 Dunbar St.', '17 West Livingston Court']
    })
print("Original DataFrame:")
print(df)

def test_and_cond(text):
    # pas d'ordre, mot non complet (99100 ok pour 9910)
    #result = re.findall(r'(?=.*Ave.)(?=.*9910).*', text) 
    result = re.findall(r'(?=.*9910)(?=.*Ave.).*', text) 
    return " ".join(result)

df['check_two_words']=df['address'].apply(lambda x : test_and_cond(x))
print("\nPresent two words (Ave. & 9910) in 'address' column:")
print(df)
