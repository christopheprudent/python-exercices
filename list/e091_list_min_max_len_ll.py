def min_max_len_ll(ll):
    ll_len = [(len(l), l) for l in ll]
    ll_len_sort = sorted(ll_len, key= lambda x: x[0])
    return ll_len_sort[0], ll_len_sort[-1]

L = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print('liste', L)
print('listes de taille minium, maximum:', min_max_len_ll(L))
L = [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
print('liste', L)
print('listes de taille minium, maximum:', min_max_len_ll(L))
L = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
print('liste', L)
print('listes de taille minium, maximum:', min_max_len_ll(L))
