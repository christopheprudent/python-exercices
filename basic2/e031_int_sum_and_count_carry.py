def count_carry(x,y):
	rx = str(x)[::-1]
	ry = str(y)[::-1]
	_carry=0
	_count_carry=0
	for i in range(min(len(rx), len(ry))):
		_x = int(rx[i:i+1])
		_y = int(ry[i:i+1])
		if _x + _y + _carry >= 10:
			_carry = 1
			_count_carry +=1
		else:
			_carry=0

	return _count_carry

print(count_carry(786, 457))
print(count_carry(5, 6))
