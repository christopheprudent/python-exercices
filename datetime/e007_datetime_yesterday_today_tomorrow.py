import datetime 

# web solution
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 
print('       hier : ',yesterday)
print('aujourd\'hui : ',today)
print('     demain : ',tomorrow)

