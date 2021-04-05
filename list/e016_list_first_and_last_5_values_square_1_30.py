def first_and_last_5_values_square_1_30(l):
	return [ x for x in l[:5] ] + [ x for x in l[-5:] ]

print(first_and_last_5_values_square_1_30([ x ** 2 for x in range(1, 31) ]))
