def items_in_minmax(l, min, max):
	t = [ x for x in l if min <= x <= max ]
	return len(t)

print(items_in_minmax([10,20,30,40,40,40,70,80,99], 40, 100))
print(items_in_minmax(['a','b','c','d','e','f'], 'a', 'e'))
