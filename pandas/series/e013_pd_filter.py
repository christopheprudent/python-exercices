import pandas as pd

s = pd.Series([0,1,2,3,4,5,6,7,8,9,10])
print(s)

# filtres
print(s[s<6])
print(s[(s<5)|(s>8)])
