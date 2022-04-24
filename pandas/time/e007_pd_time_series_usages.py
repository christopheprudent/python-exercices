import pandas as pd
index = pd.DatetimeIndex(['2011-09-02', '2012-08-04',
                          '2015-09-03', '2010-08-04',
                          '2015-03-03', '2011-08-04',
                          '2015-04-03', '2012-08-04'])

s_dates = pd.Series([0, 1, 2, 3, 4, 5, 6, 7], index=index)

print("Time series object with indexed data:")
print(s_dates)
print("\nDates of same year (2015):")
print(s_dates['2015'])

# WARN: FutureWarning: Value based partial slicing on non-monotonic DatetimeIndexes with non-existing keys is deprecated and will raise a KeyError in a future Version.
# print(s_dates['2012-01-01':'2012-12-31']) 
# https://stackoverflow.com/questions/66116893/iterating-through-dictionaries-futurewarning-value-based-partial-slicing-on-n
print("\nDates between 2012-01-01 and 2012-12-31")
print(s_dates.sort_index().loc['2012-01-01':'2012-12-31']) 
