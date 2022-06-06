import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')

print("World alcohol consumption sample data:")
print(w_a_con.head())

print("\nFind  all columns which all entries present:")
all_notnull = w_a_con.loc[:, w_a_con.notnull().all()]
print(all_notnull.count())

print("\nRows and columns has a NaN:")
any_isnull = w_a_con.loc[:,w_a_con.isnull().any()]
print(any_isnull.count())

print("\nDrop rows with any NaNs:")
print(w_a_con.dropna(how='any'))  
