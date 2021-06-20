L1 = [1, 2, 3]
L2 = [4, 5, 6]

print('listes', L1, L2)
print('ajout des éléments:', list(map(lambda x: x[0]+x[1], zip(L1, L2))))

# web solution
# https://www.geeksforgeeks.org/python-map-function/
result = map(lambda x, y: x + y, L1, L2)
print(list(result))
