# sum 2 ints, but return 20 if 15<=sum<=20

values = []
_sum = 0
for i in range(2):
	values.append(int(input('Entrez un nombre : ')))
	_sum += values[i]

if (_sum >= 15 and _sum <= 20):
	_sum = 20

print('La somme combinée est égale à ', _sum)
