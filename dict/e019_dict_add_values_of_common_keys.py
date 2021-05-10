def add_values_of_common_keys(d1, d2):
    d = dict()
    for k in d1.keys():
        if k in d2:
            d[k] = d1[k] + d2[k]
        else:
            d[k] = d1[k]

    for k in d2.keys():
        if not k in d1:
            d[k] = d2[k]

    return d

D1 = {'a': 100, 'b': 200, 'c':300}
D2 = {'a': 300, 'b': 200, 'd':400}
print('dictionnaire1', D1)
print('dictionnaire2', D2)
print('cumul des dictionnaires, en additionnant les valeurs pour les clés communes')
print(add_values_of_common_keys(D1, D2)) 

# web solution
from collections import Counter
D = Counter(D1) + Counter(D2)
print(D)
