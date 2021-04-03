def add_if_int(obj1, obj2):
	if (type(obj1) == type(obj2) == int):
		return (obj1+obj2)

	return None

_obj1 = 12
_obj2 = 3
print('add_if_int=', add_if_int(_obj1, _obj2))
_obj1 = 12.5
print('add_if_int=', add_if_int(_obj1, _obj2))
_obj1 = '12.5'
print('add_if_int=', add_if_int(_obj1, _obj2))
