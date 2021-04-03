# sum 2 ints, return True they are the same or their sum or difference is 5

values = []
_sum = 0
for i in range(2):
	values.append(int(input('Entrez un nombre : ')))
	_sum += values[i]

_rc = False
if (values[0] == values[1] or _sum == 5 or abs(values[0] - values[1]) == 5):
	_rc = True

print('Le résultat est', _rc)
