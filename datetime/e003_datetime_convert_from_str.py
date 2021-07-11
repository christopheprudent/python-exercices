from datetime import datetime

date_time_str = '18/09/19 01:55:19'
print('test 1 (%s)' % date_time_str)
date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
print("type de la  date", type(date_time_obj))
print("valeur de la date", date_time_obj)

# web solution
date_time_str = 'Jul 1 2014 2:43PM'
print('test 2 (%s)' % date_time_str)
date_object = datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
print(date_object)
