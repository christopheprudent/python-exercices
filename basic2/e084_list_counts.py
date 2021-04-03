def counts(a):
	_n_negative=0
	_sum_positive=0

	for v in a:
		if v < 0:
			_n_negative += 1
		else:
			_sum_positive += v

	return [_n_negative, _sum_positive]

print(counts([1, 2, 3, 4, 5]))
print(counts([-1, -2, -3, -4, -5]))
print(counts([1, 2, 3, -4, -5]))
print(counts([1, 2, -3, -4, -5]))
