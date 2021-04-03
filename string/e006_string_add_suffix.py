def add_suffix(s):
	if len(s) < 3:
		return s

	if s[-3:] == 'ing':
		return s + 'ly'
	else:
		return s + 'ing'

print(add_suffix('ab'))
print(add_suffix('abc'))
print(add_suffix('string'))
		
