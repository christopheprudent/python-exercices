def iter_pairs(l):
    return [(l[i], l[i+1]) for i in range(len(l) -1)]

L = [1, 1, 2, 3, 3, 4, 4, 5]
print('liste', L)
print('chaque pair des éléments', iter_pairs(L))
