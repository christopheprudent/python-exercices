def in_list(list, item):
	if item in list:
		return True

	return False

list1=[1, 5, 8, 3]
print('Item %i in list [%s] : %s'%(5, ', '.join(map(str, list1)), in_list(list1, 5)))
print('Item %i in list [%s] : %s'%(0, ', '.join(map(str, list1)), in_list(list1, 0)))
