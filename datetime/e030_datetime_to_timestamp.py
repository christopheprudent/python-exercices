import datetime, time

_date = datetime.datetime.now()
print('timetuple:', _date.timetuple())
print('timestamp:', time.mktime(_date.timetuple()))

_date2 = datetime.datetime(2016, 2, 25, 23, 23)
print('timetuple:', _date2.timetuple())
print('timestamp:', time.mktime(_date2.timetuple()))
