import pandas as pd
result = pd.Series(pd.date_range('2022-01-01', periods=52, freq='W-SUN'))
print("All Sundays of 2022:")
print(result)
