import array

A = array.array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print('tableau', A)
print('suppression 1ère occurrence de la valeur 3')
A.remove(3)
print('tableau', A)
