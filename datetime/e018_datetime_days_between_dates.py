import datetime

d1 = datetime.date(2000, 2, 28)
d2 = datetime.date(2001, 2, 28)
print('date 1', d1)
print('date 2', d2)

days = (d2 - d1).days
print('écart            entre ces 2 dates :', d2 - d1)
print('écart (en jours) entre ces 2 dates :', days)
