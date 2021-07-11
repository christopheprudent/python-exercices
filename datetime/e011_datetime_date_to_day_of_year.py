import datetime

date_str = input('Entrez une date AA/MM/JJ: ')
#date_items = date_str.split('/')
date_obj = datetime.datetime.strptime(date_str, '%y/%m/%d')
print('la date saisie', date_obj, 'correspond au', date_obj.strftime("%j"), 'jour de l\'année')

# web solution
day_of_year = (date_obj - datetime.datetime(date_obj.year, 1, 1)).days + 1
print(day_of_year)
