import calendar, pprint

#print('avec premier jour de la semaine : ', calendar.firstweekday(), calendar.MONDAY, calendar.SUNDAY)

_year = int(input('Entrez une année (AAAA) : '))
_month = int(input('Entrez un mois : '))
_ndays = calendar.monthrange(_year, _month)[1]

_weekdays = [
    'lundi'
  , 'mardi'
  , 'mercredi'
  , 'jeudi'
  , 'vendredi'
  , 'samedi'
  , 'dimanche'
]

#for _i in range(len(_weekdays)):
#    print(f'i={_i} jour={_weekdays[_i]}')

print('dernier jour du mois est : %d/%d/%d (%s)' %(_ndays, _month, _year, _weekdays[calendar.weekday(_year, _month, _ndays)]))
pprint.pprint(calendar.monthcalendar(_year, _month))
