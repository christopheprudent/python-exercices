import copy

S = set(range(1,11))
print('set', S)
print('copie dans S2')
S2 = copy.copy(S)
print('S2', S2)

print('ajout élément dans S')
S.add(20)
print(' S', S)
print('S2', S2)

# web solution
print('copie dans S3')
S3 = S.copy()
print('S3', S3)
