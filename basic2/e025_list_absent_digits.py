def absent_digits(lnums):
	lad = [i for i in range(10) if not i in lnums]
	return lad

print('Les chiffres absents de la liste %s sont %s' %([9,8,3,2,2,0,9,7,6,3], absent_digits([9,8,3,2,2,0,9,7,6,3])))
