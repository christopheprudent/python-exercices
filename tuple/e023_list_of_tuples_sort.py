L = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print('liste', L)
print('après tri inversé 2e colonne (en nombre flottant)')
print(sorted(L, key= lambda x: float(x[1]), reverse=True))
