import datetime 

today = datetime.date.today()
print('aujourd\'hui : ', today)
for day in range(1, 6):
    next_day = today + datetime.timedelta(days = day) 
    print('suivant: ', next_day)
