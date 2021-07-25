import datetime

date_str = input('Entrez une date AA/MM/JJ: ')
date_obj = datetime.datetime.strptime(date_str, '%y/%m/%d')
print('la date saisie', date_obj, 'correspond à la semaine', date_obj.strftime("%W"), 'de l\'année')

# web solution
print(datetime.date(date_obj.year, date_obj.month, date_obj.day).isocalendar()[1])
