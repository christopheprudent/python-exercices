# https://stackoverflow.com/questions/9637838/convert-string-date-to-timestamp-in-python
import time
import datetime
s = "01/12/2011"
print('date:', s)
print('timestamp:', time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))
print('timestamp:', time.mktime(time.strptime(s, "%d/%m/%Y")))
