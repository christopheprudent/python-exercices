def groups_non_value_items(l, value):
    _n = 0
    _groups = []
    for i, x in enumerate(l):
        if x == value:
            if _n > 0:
                _groups.append((i-_n,i))
                _n = 0
        else:
            _n += 1

    if _n > 0:
        i += 1
        _groups.append((i-_n,i))
    return _groups

L = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
print('liste', L)
print('ensemble des groupes de valeurs (début, fin) sans la valeur {}'.format(0))
print('taille liste', len(L))
# [(0, 4), (10, 15), (20, 26), (32, 38)]
groups = groups_non_value_items(L, 0)
print(groups)
print('nombre de groupe(s), séparés par la valeur {}'.format(0))
print(len(groups))
print('valeurs de ces groupe(s)')
print([L[i:j] for (i,j) in groups])
print('somme de ces groupe(s)')
print([sum(L[i:j]) for (i,j) in groups])
