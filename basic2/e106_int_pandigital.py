def is_pandigital(i, b=10):
	d = [ str(x) for x in range(b) ]
	si = str(i)
	return all(x in si for x in d)

# web solution
def is_pandigital_num(n):
    return len(set(str(n))) == 10

print(is_pandigital(1023456897))
print(is_pandigital(1023456798))
print(is_pandigital(1023457689))
print(is_pandigital(1023456789))
print(is_pandigital(102345679))
print(is_pandigital(14320, 5))
