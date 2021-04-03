def substrat_sum_digits(n):
	print('n=%d' % n)
	_sum = 0
	for d in str(n):
		_sum += int(d)

	n -= _sum
	if n > 0:
		substrat_sum_digits(n)


n = int(input('Entrez un nombre entier : '))
substrat_sum_digits(n)

