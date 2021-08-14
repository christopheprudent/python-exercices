import datetime

_date = datetime.date(2015, 1, 1)
_gap = 20

for _nof in range(1, 13):
    _new_date = _date + datetime.timedelta(days = (_nof * _gap))
    print('nouvelle date avec écart de', _nof, 'fois 20 jours :', _new_date)
