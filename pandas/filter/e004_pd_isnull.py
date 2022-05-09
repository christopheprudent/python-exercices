import pandas as pd
import numpy as np

# World alcohol consumption data
w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nMissing values:")
print(w_a_con.isnull())

print("\nfind missing values:")
_isnull = np.where(pd.isnull(w_a_con))
print(_isnull)
_isn_rows = _isnull[0]
_isn_cols = _isnull[1]

for i in range(len(_isn_rows)):
    print(w_a_con.iloc[_isn_rows[i]])
    print('data [%d, %d] = %s' % (_isn_rows[i], _isn_cols[i], w_a_con.iloc[_isn_rows[i], _isn_cols[i]]))
#    print(' row', _isn_rows[i])
#    print(' col', _isn_cols[i])
#    print('data', w_a_con.iloc[_isn_rows[i], _isn_cols[i]])

print("\nDropping the missing values:")
print(w_a_con.dropna())
