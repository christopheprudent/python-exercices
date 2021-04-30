def smallest_number(l):
    return ''.join(sorted(map(str, l)))

L = [3, 40, 41, 43, 74, 9]
print('liste', L)
print('trié pour obtenir le plus grand nombre', smallest_number(L))

L = [10, 40, 20, 30, 50, 60]
print('liste', L)
print('trié pour obtenir le plus grand nombre', smallest_number(L))

L = [8, 4, 2, 9, 5, 6, 1, 0]
print('liste', L)
print('trié pour obtenir le plus grand nombre', smallest_number(L))
