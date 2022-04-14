import pandas as pd
s = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
print('serie')
print(s)
index = ['B','A','C','D','E']
s = s.reindex(index = index)
print('après changement d\'ordre', index)
print(s)
