import itertools

n = int(input('Entrez un nombre entier : '))
comb = []
for item in itertools.product(range(10), range(10), range(10), range(10)):
	if sum(item) == n:
		comb.append(item)

print('Il y a %d combinaisons possibles, soit %s' %(len(comb), comb))

