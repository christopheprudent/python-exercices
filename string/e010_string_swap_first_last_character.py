def swap_first_last_character(s):

	# web solution
	return s[-1:] + s[1:-1] + s[:1]

	n = len(s)
	if n > 0:
		ns=s[-1] + s[1:n-1] + s[0]
		return ns
	else:
		return s

print(swap_first_last_character(''))
print(swap_first_last_character('python'))
