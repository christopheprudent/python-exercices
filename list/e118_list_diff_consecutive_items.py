def diff_consecutive_items(l):
    return [y-x for x, y in zip(l, l[1:])]

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Liste', L)
print('diff (i+1, i):', diff_consecutive_items(L))

L = [2, 4, 6, 8]
print('Liste', L)
print('diff (i+1, i):', diff_consecutive_items(L))
