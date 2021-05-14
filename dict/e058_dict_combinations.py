import itertools

D = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
print('dictionnaire', D)
print('combinaisons des clés/valeurs')
print(list(map(dict, itertools.combinations(D.items(), 2))))

D = {'V' : [1, 3, 5], 'VI' : [1, 5]}
print('dictionnaire', D)
print('combinaisons des clés/valeurs')
print(list(map(dict, itertools.combinations(D.items(), 2))))
