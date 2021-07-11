import datetime

now = datetime.datetime.now()
today = datetime.date.today()
print('date/heure courante', now.strftime('%Y-%m-%d-%H:%M:%S'))
print('année:', now.year, today.strftime("%Y"))
print('mois:', now.month, today.strftime("%m (%B)"))
print('jour:', now.day, today.strftime("%d"), '(année)', today.strftime("%j"), '(semaine)', today.strftime("%w"))
