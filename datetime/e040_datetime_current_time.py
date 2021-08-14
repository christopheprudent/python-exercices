import datetime, time
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')

_today = datetime.date.today()
_now = datetime.datetime.now()

print('timestamp (EPOCH):', time.time())
print('date & heure courante:', _now)
print('date & heure courante:', _now.strftime("%d/%m/%y %H:%M:%S"))
print('année:', _today.strftime("%Y"))
print('mois:', _today.strftime("%B"))
print('semaine:', _today.strftime("%W"))
print('id jour semaine:', _today.strftime("%w"))
print('jour année:', _today.strftime("%j"))
print('jour mois:', _today.strftime("%d"))
print('jour semaine:', _today.strftime("%A"))
