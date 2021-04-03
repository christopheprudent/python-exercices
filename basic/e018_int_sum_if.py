# sum 3 ints, but double it if 3 are the same!

values = []
_sum = 0
for i in range(3):
	values.append(int(input('Entrez un nombre : ')))
	_sum += values[i]

_factor = 3 if ((_sum / 3) == values[0]) else 1
print('La somme combinée est égale à ', _sum * _factor)
