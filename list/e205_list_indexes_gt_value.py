def indexes_gt_value(l, value):
    return [i for i,x in enumerate(l) if x > value]

L = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
print('liste', L)
print('ensemble des indices, pour lesquels la valeur est supérieure à {}'.format(3000))
print(indexes_gt_value(L, 3000))

print('ensemble des indices, pour lesquels la valeur est supérieure à {}'.format(20000))
print(indexes_gt_value(L, 20000))
