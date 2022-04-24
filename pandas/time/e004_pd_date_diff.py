import pandas as pd
from datetime import datetime, date

today = datetime(2012, 10, 30)
print("As current date:", today)
tomorrow = today + pd.Timedelta(days=1)
print("Tomorrow:", tomorrow)
yesterday = today - pd.Timedelta(days=1)
print("Yesterday:", yesterday)

date1 = datetime(2016, 8, 2)
date2 = datetime(2016, 7, 19)
print("\nDifference between two dates (d1=%s) (d2=%s) : d1-d2=%s" % (date1, date2, (date1 - date2)))
