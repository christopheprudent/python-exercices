def concat_uncommon_chars(s1, s2):
	ns = ''
	uc1 = [ c for c in s1 if c not in s2 ]
	uc2 = [ c for c in s2 if c not in s1 ]
	return ''.join(uc1 + uc2)

print(concat_uncommon_chars('abcdpqr', 'xyzabcd'))
	
