def is_narcissistic(n):
	ns = str(n)
	if not ns.isdigit():
		return False

	l = len(ns)
	s = 0
	for d in ns:
		s += int(d) ** l

	return (s == n)

# web solution
def is_narcissistic_num(num):
	return num == sum([int(x) ** len(str(num)) for x in str(num)])

print(is_narcissistic(153))
print(is_narcissistic(370))
print(is_narcissistic(407))
print(is_narcissistic(409))
print(is_narcissistic(1634))
print(is_narcissistic(8208))
print(is_narcissistic(9474))
print(is_narcissistic(9475))
