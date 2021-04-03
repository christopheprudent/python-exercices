def str_first_last(s, f=2, l=2):
	if len(s) < max(f, l):
		return ''

	return s[:f] + s[-l:]

print(str_first_last('w3resource'))
print(str_first_last('w3'))
print(str_first_last('w'))
