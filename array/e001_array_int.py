import array

A = array.array('i', [1, 3, 5 , 7, 9])
print('tableau', A)
print('ensemble des éléments')
for x in A:
    print(x)
print('accès par index aux éléments')
for i in range(3):
    print('index {} valeur {}'.format(i, A[i]))
