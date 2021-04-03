def insert_end(s, dup=4):
	if len(s) > 2:
		return s[-2:] * dup
	else:
		return ''

print(insert_end('Python'))
print(insert_end('Exercises', 3))
print(insert_end('', 2))
