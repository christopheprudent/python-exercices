def list_to_string(l):
	return ''.join(map(str, l))

lst = [11, 33, 50]
print('liste={}'.format(lst))
print(list_to_string(lst))
