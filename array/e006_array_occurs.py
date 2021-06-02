import array

A = array.array('i', [1, 3, 5, 3, 7, 9, 3])
print('tableau', A)
print('nb occurrence(s) de {} : {}'.format(3, A.count(3)))
