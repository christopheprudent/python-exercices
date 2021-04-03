def sum_digits(s):
	d = [ int(d) for d in s if d.isdigit() ]
	return sum(d)

print(sum_digits("123abcd45"))
print(sum_digits("abcd1234"))
