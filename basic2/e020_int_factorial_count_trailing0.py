import math
import re

def count_ending_factorial(n, ending):
	if not (n >= 1 and n <= 2*109):
		raise ValueError

	fact = math.factorial(n)
	with_ending = re.search('(' + ending + '*)$', str(fact))
	return (fact, len(with_ending.group(1)))

n = int(input('Entrez un nombre entier: '))
fact, ending0 = count_ending_factorial(n, '0')
print('dans %d!=%d, il y a %d 0 à la fin' %(n, fact, ending0))
	
