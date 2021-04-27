L = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
print('liste', L)
print('intersection des sous-listes', list(set.intersection(*map(set,L))))

L = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
print('liste', L)
print('intersection des sous-listes', list(set.intersection(*map(set,L))))
