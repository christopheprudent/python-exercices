def difference(n):
	'''Calculate difference of argument w/ 17, print it or its double if n > 17'''

	_delta = n - 17
	#print('Difference de %i avec 17 égal à %i' %(n, _delta if (n <= 17) else _delta * 2))
	return _delta if (n <= 17) else _delta * 2

#difference(15)
#difference(25)
print('Difference de %i avec 17 égal à %i' %(15, difference(15)))
print('Difference de %i avec 17 égal à %i' %(25, difference(25)))
