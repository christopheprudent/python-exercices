import pandas as pd

# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')

print("World alcohol consumption sample data:")
print(w_a_con.head())

print("\nFrom the 'Year' column, access other column (w/ step of 2), by name :")
print(w_a_con.loc[:,'Year'::2].head(5))
print("\nAlternate solution, by id:")
print(w_a_con.iloc[:,0::2].head(5))
