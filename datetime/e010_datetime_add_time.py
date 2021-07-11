import datetime

# web solution
x = datetime.datetime.now()
y = x + datetime.timedelta(seconds=5)
print('heure courante', x.time())
print('+ 5 secondes', y.time())
