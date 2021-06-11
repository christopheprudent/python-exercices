import random

start = 1
stop = 9
r = random.randrange(start, stop)

while True:
    n = int(input('entrez le nombre entre {} et {} pour trouver le nombre caché'.format(start, stop)))
    if n == r:
        print('bien joué, le nombre était bien {}'.format(r))
        break
    else:
        print('retentez votre chance!')
