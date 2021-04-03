n = int(input('Entrez un nombre entier positif :'))

_sum = 0
for _i in range(1, n):
	_sum += (_i ** 3)

print('Somme des valeurs cubiques de 1 à ', n -1, ' vaut : ', _sum)
