def reverse_only_vowels(s):
	'''
	inverse les lettres de type voyelle seulement (pas celle de type consonne)
	'''
	vs = s[::-1]
	ns = ''
	for i, c in enumerate(s):
		if not c.lower() in 'aeiouy':
			ns += s[i]
		else:
			ns += vs[i]

	return ns

print(reverse_only_vowels('w3resource'))
print(reverse_only_vowels('Perl'))
print(reverse_only_vowels('USA'))


