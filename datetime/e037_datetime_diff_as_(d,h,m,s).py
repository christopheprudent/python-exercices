import datetime, time

_date1 = datetime.datetime(2016, 2, 25, 23, 23, 10)
_date2 = datetime.datetime(2016, 3, 11, 14, 45, 24)
_timedelta = _date2 - _date1

print('date 1:', _date1)
print('date 2:', _date2)

_days = _timedelta.days
#_hours = int(_timedelta.seconds / 3600)
_hours = _timedelta.seconds // 3600
#_minutes = int((_timedelta.seconds - (_hours * 3600)) / 60)
_minutes = (_timedelta.seconds - (_hours * 3600)) // 60
_seconds = _timedelta.seconds - (_hours * 3600) - (_minutes * 60)

print('diff  :', _timedelta)
print(' (j)  :', _days)
print(' (h)  :', _hours)
print(' (m)  :', _minutes)
print(' (s)  :', _seconds)
