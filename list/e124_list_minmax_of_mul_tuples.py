L = [(2, 7), (2, 6), (1, 8), (4, 9)]
print('liste', L)
print('min produit de chaque couple', min(x[0]*x[1] for x in L), min(x*y for x,y in L))
print('max produit de chaque couple', max(x[0]*x[1] for x in L), max(x*y for x,y in L))
