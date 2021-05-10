import itertools
D = {'1':['a','b'], '2':['c','d'], '3':['e', 'f']}
print('dictionnaire', D)
print('lettres de chaque clé', [D[k] for k in D.keys()])
print('combinaisons avec les lettres de deux clés différentes')
combi = itertools.product(*[D[k] for k in D.keys()])
# [('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd')]
print(list(combi))
print('sous forme de chaînes')
combi = itertools.product(*[D[k] for k in D.keys()])
for x in combi:
    print(''.join(x))
#ac
#ad
#bc
#bd
