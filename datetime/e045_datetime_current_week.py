import datetime

now = datetime.datetime.now()
_year, _week, _day_of_week = now.isocalendar()

print('date actuelle: année=%d, semaine=%d, jour semaine=%d' % (_year, _week, _day_of_week))
