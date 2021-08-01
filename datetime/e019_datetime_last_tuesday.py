import datetime

_today = datetime.date.today()
_tuesday = _today + datetime.timedelta(days = 1 - _today.weekday())
print('date du jour : ', _today)
print('date du dernier mardi : ', _tuesday)
