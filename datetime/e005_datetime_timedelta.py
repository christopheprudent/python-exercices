import datetime

today = datetime.datetime.today()
print('date courante', today)
today_minus_5d = today + datetime.timedelta(days=-5)
print('moins 5j', today_minus_5d)
