import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')

print("World alcohol consumption sample data:")
print(w_a_con.head())

who_region = ["Africa", "Eastern Mediterranean", "Europe"]
print("\nFilter by matching multiple values in a given dataframe, in given list:", who_region)
flt_wine = w_a_con["WHO region"].isin(who_region)
print(w_a_con[flt_wine])

print("\nSelect all rows which not appears in a given list:", who_region)
flt_wine = ~w_a_con["WHO region"].isin(who_region)
print(w_a_con[flt_wine])
