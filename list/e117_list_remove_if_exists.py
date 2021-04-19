def remove_if_exists(l1, l2):
    return [ x for x in l1 if x not in l2 ]

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L2 = [2, 4, 6, 8]

print('liste', L1)
print('sans les éléments de {} : {}'.format(L2, remove_if_exists(L1, L2)))
