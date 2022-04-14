import pandas as pd
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
print('série')
print(sr1)
print('série')
print(sr2)
print('not in')
result = sr1[~sr1.isin(sr2)]
print(result)
