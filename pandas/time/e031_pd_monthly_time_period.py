import pandas as pd

mtp = pd.Period('2022-05','M')
print("Monthly time period: ", mtp)

print("\nList of names in the current local scope:")
print(dir(mtp)) 

print('isleap', mtp.is_leap_year)
print(mtp.day)
print(mtp.day_of_week)
print(mtp.day_of_year)
#for m in ['day', 'day_of_week', 'day_of_year', 'dayofweek', 'dayofyear', 'days_in_month', 'daysinmonth']:
for m in ['start_time', 'end_time', 'strftime']:
    print('member:', m)
    print('value:', eval('mtp.' + m))
