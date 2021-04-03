def get_lowest_highest(s):
	l = sorted([ int(x) for x in s.split()])
	return (l[0], l[-1])

print(get_lowest_highest("1 4 5 77 9 0"))
print(get_lowest_highest("-1 -4 -5 -77 -9 0"))
print(get_lowest_highest("0 0"))
