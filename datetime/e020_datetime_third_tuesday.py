import datetime

_year = int(input('Entrez une année (AAAA) : '))
_month = int(input('Entrez un mois : '))
_date = datetime.date(_year, _month, 1)

if _date.weekday() <= 1:
    _days = 1 - _date.weekday()
else:
    _days = 7 - _date.weekday() +1

_1st_tuesday = _date + datetime.timedelta(days = _days)
print('date saisie             : ', _date)
print('date du premier mardi   : ', _1st_tuesday)
print('date du troisième mardi : ', _1st_tuesday + datetime.timedelta(days = 14))
