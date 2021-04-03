s = input('Entrez un mot : ')
#n = sum([1 if c.isupper() for c in s[:4]])
n = sum(1 for c in s[:4] if c.isupper())
#n = sum([1 for c in s[:4] if c.isupper() ])
if n >= 2:
	print(s.upper())
