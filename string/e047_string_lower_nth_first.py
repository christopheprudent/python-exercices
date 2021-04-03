def lower_nth_first(s, n):
	return ''.join([ c.lower() if i < n else c for i, c in enumerate(s) ])

print(lower_nth_first('HELLO world!', 5))
print(lower_nth_first('Hello World!', 7))
print(lower_nth_first('Hello WORLD!', 7))
