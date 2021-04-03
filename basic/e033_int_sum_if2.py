# sum 3 ints, but equal 0 if 2 are the same!

values = []
_sum = 0
for i in range(3):
	values.append(int(input('Entrez un nombre : ')))
	_sum += values[i]

_factor = 0 if (values[0] == values[1] or values[0] == values[2] or values[1] == values[2]) else 1
print('La somme combinée est égale à ', _sum * _factor)
