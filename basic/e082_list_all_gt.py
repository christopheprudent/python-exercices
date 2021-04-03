def all_gt(list, than):
	_set=set(list)
	for _t in _set:
		if (_t <= than):
			return False 

	return True

testList = [2, 45, 7, 4, 2, 119]
print(all_gt(testList, 3))
print(all_gt(testList, 1))

print(all(x > 3 for x in testList))
print(all(x > 1 for x in testList))
