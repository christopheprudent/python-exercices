import array

A = array.array('i', [1, 3, 5 , 7, 9])
print('tableau', A)
info = A.buffer_info()
print('info mémoire: adresse={}'.format(info[0]))
print('info mémoire: #éléments={}'.format(info[1]))
print('info mémoire: taille tampon={}'.format(info[1] * A.itemsize))
