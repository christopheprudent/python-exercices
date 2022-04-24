import pandas as pd

print("\nA specific date using timestamp:")
print(pd.Timestamp('2016-11-10'))
print("\nDate and time using timestamp:")
print(pd.Timestamp('2012-05-03 11:30'))
print("\nA time adds in the current local date using timestamp:")
print(pd.Timestamp('11:30'))
print("\nCurrent date and time using timestamp:")
print(pd.Timestamp("now"))
