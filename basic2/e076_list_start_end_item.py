def start_end_item(a, item):
	_start=0
	_end=0
	_found = False

	for i, v in enumerate(a):
		if v == item:
			if not _found:
				_found = True
				_start = i

			_end = i

		if v > item:
			break

	return [_start, _end]

data = [5, 7, 7, 8, 8, 8]
item = 8
print('Recherche positions {0} dans {1} : {2[0]}, {2[1]}'.format(item, data, start_end_item(data, item)))

data = [1, 3, 6, 9, 13, 14]
item = 4
print('Recherche positions {0} dans {1} : {2[0]}, {2[1]}'.format(item, data, start_end_item(data, item)))

