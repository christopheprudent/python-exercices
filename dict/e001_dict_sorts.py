import operator

D = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('dictionnaire', D)

print('trié par clé (ordre croissant)')
print(sorted(D.items(), key=lambda x:x[0]))
print(sorted(D.items(), key=operator.itemgetter(0)))
print('trié par clé (ordre décroissant)')
print(sorted(D.items(), key=lambda x:x[0], reverse=True))
print(sorted(D.items(), key=operator.itemgetter(0), reverse=True))

print('trié par valeur (ordre croissant)')
print(sorted(D.items(), key=lambda x:x[1]))
print(sorted(D.items(), key=operator.itemgetter(1)))
print('trié par valeur (ordre décroissant)')
print(sorted(D.items(), key=lambda x:x[1]))
print(sorted(D.items(), key=operator.itemgetter(1), reverse=True))
