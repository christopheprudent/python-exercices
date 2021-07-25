import datetime
def all_sundays_of_year(y):
    _date = datetime.date(y, 1, 1)
    while True:
        if _date.year != y:
            break

        if datetime.datetime.strftime(_date, '%w') == '0':
            yield _date

        _date += datetime.timedelta(days=1)

# web solution
def all_sundays(year):
    # January 1st of the given year
    dt = datetime.date(year, 1, 1)
    # First Sunday of the given year       
    dt += datetime.timedelta(days = 6 - dt.weekday())  
    while dt.year == year:
       yield dt
       dt += datetime.timedelta(days = 7)

print('Trouver la date de tous les dimanches d\'une année')
_year = int(input(('Entrez l\'année : ')))

print(list(all_sundays_of_year(_year)))
for s in all_sundays(_year):
   print(s)
