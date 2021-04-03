def first_three(s):
	# web solution
	return s[:3] if len(s) > 3 else s

	if len(s) < 3:
		return s
	else:
		return s[:3]

print(first_three('ipy'))
print(first_three('python'))
