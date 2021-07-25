import datetime

date_obj = datetime.datetime.strptime("2015 50 1", "%Y %W %w")
print('la date du lundi de la semaine %d de l\'année %d : %s' %(50, 2015, datetime.datetime.strftime(date_obj, '%d/%m/%Y')))
