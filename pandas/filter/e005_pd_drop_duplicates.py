import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())

print("\ncount rows of each WHO region")
print(w_a_con.groupby('WHO region').size())

print("\nAfter removing the duplicates of WHO region column:")
print(w_a_con.drop_duplicates('WHO region'))
