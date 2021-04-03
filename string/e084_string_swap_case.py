def swap_case(s):
	sc = [ c.upper() if c.islower() else c.lower() for c in s ]
	return sc

s = input('Entrez une chaine : ')
print(''.join(swap_case(s)))
