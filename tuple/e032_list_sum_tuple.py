def sum_tuples_of_list(l):
    return list(map(sum, l))

L=[(1, 2), (2, 3), (3, 4)]
print('liste', L)
print('somme de ses tuples')
#[3, 5, 7]
print(sum_tuples_of_list(L))

L=[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
print('liste', L)
print('somme de ses tuples')
#[9, -1, 7, 8]
print(sum_tuples_of_list(L))
