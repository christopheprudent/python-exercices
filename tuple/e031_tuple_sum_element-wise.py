t1=(1, 2, 3, 4)
t2=(3, 5, 2, 1)
t3=(2, 2, 3, 1)
print('tuple 1', t1)
print('tuple 2', t2)
print('tuple 3', t3)
print('tuple résultat avec les éléments de chaque niveau')
#((1, 3, 2), (2, 5, 2), (3, 2, 3), (4, 1, 1))
print(tuple(zip(t1, t2, t3)))

print('somme de ces tuples résulats')
#(6, 9, 8, 6)
print(tuple(sum(x) for x in zip(t1, t2, t3)))

# web solution
print(tuple(map(sum, zip(t1, t2, t3))))
