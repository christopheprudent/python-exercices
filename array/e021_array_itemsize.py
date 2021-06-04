import array

A = array.array('I', [1, 3, 5 , 7, 9])
print('tableau', A)
print('taille élément', A.itemsize)

A = array.array('f', [1.0, -3.05, 5.1 , 7.0, 9.005])
print('tableau', A)
print('taille élément', A.itemsize)
