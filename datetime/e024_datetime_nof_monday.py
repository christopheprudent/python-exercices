import datetime

_2015_1_1 = datetime.date(2015, 1, 1)
_2016_1_1 = datetime.date(2016, 1, 1)

_nof_days = (_2016_1_1 - _2015_1_1).days
_nof_mondays = int(_nof_days / 7)
print('nombre de jours entre', _2016_1_1, 'et', _2015_1_1, ':', _nof_days, 'soit:', _nof_mondays, 'lundi!')

# web solution (nombre de lundi en début de mois!)
_nof_mondays = 0
for _year in range(2015, 2017):
    for _month in range(1, 13):
        if datetime.date(_year, _month, 1).weekday() == 0:
            _nof_mondays += 1 
print('nombre de lundi (en début de mois):', _nof_mondays)
