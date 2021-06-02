import array

A = array.array('i', [1, 3, 5 , 7, 9])
print('tableau', A)
e = 11
print('ajout élément {}'.format(e))
A.append(e)
print('tableau', A)
