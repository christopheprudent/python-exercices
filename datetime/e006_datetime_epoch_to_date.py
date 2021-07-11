import datetime

todate = datetime.datetime.fromtimestamp(1284105682)
# résultat attendu: 2010-09-10 13:31:22
# résultat obtenu: 2010-09-10 10:01:22
print(todate)

# web solution
print(
    datetime.datetime.fromtimestamp(
        int("1284105682")
    ).strftime('%Y-%m-%d %H:%M:%S')
)
