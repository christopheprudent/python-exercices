import pandas as pd
import numpy as np
s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'])
print("serie w/ date as string:")
print(s)
r = pd.to_datetime(pd.Series(s))
print("serie w/ string converted to datetime:")
print(r)
df = pd.DataFrame(r)
print("Original DataFrame (string to datetime):")
print(df)
