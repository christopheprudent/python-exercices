def join_lists_of_lists(ll1, ll2):
    return [x+y for x, y in zip(ll1, ll2)]

L1 = [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
L2 = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
print('liste 1:', L1)
print('liste 2:', L2)
print('concaténation des sous-listes', join_lists_of_lists(L1, L2))
