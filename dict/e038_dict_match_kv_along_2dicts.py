def match_kv_from_2dicts(d1, d2):
    return [(k,v) for k,v in d1.items() if k in d2.keys() and d2[k] == d1[k]]

D1 = {'key1': 1, 'key2': 3, 'key3': 2}
D2 = {'key1': 1, 'key2': 2}
print('dictionnaire 1', D1)
print('dictionnaire 2', D2)
print('ensemble des (clé,valeur) communs aux 2 dictionnaires')
print(match_kv_from_2dicts(D1, D2))

# web solution
print('ensemble 1', set(D1.items()))
print('ensemble 2', set(D2.items()))
for (key, value) in set(D1.items()) & set(D2.items()):
    print('%s: %s est présent dans les 2 dictionnaires' % (key, value))
