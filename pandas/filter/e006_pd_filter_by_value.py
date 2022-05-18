import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())

print("\nThe world alcohol consumption details in the year 1985:")
print(w_a_con[w_a_con['Year']==1985].head(10))

print("\nThe world alcohol consumption details in the years 1987 and 1989:")
print((w_a_con[(w_a_con['Year']==1987) | (w_a_con['Year']==1989)]).head(10))

print("\nThe world alcohol consumption details in the year 1985 and in 'Americas' region:")
print((w_a_con[(w_a_con['Year']==1985) & (w_a_con['WHO region']=='Americas')]).head(10))

print("\nFiltering records by label or index:")
print(w_a_con.loc[0:4, ["WHO region", "Beverage Types"]])

print("\nMatch if  a given column has the particular sub string as 'Ea':")
print(w_a_con[w_a_con["WHO region"].str.contains("Ea")])
