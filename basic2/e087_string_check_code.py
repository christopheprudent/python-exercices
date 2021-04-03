def check_code(s):
	'''
	check code to return True if composed of 8 or 12 digits
	'''
	_n=0
	for d in s:
		if d in '0123456789':
			_n += 1

	return ((_n == 8 == len(s)) or (_n == 12 == len(s)))

print(check_code('12345678'))
print(check_code('1234567j'))
print(check_code('12345678j'))
print(check_code('123456789123'))
print(check_code('123456abcdef'))
