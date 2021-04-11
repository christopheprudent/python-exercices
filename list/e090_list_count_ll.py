L = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
print('liste', L)
print('nombre de liste(s):', sum(1 for l in L if isinstance(l, list)))

L2 = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
print('liste', L2)
print('nombre de liste(s):', sum(1 for l in L2 if isinstance(l, list)))
