import pandas as pd
from pandas.tseries.offsets import BusinessDay, BMonthEnd
from datetime import datetime, date

dt = datetime(2022, 5, 5)
print("Specified date:")
print(dt)

print("\nOne business day from the said date:")
obday = dt + BusinessDay()
print(obday)
print("\nTwo business days from the said date:")
tbday = dt + 2 * BusinessDay()
print(tbday)
print("\nThree business days from the said date:")
thbday = dt + 3 * BusinessDay()
print(thbday)
print("\nNext business month end from the said date:")
nbday = dt + BMonthEnd()
print(nbday)
