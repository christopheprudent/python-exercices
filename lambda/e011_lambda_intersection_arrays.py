inter = lambda a1, a2 : list(set(a1) & set(a2))

# web solution

L1 = [1, 2, 3, 5, 7, 8, 9, 10]
L2 = [1, 2, 4, 8, 9]

print('listes', L1, L2)
print('intersection: ', 'me', inter(L1, L2), 'web', list(filter(lambda x: x in L1, L2)))
