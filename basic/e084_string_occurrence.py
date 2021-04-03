def occurrence(s, c):
	_occ=0
	for _c in s:
		if _c == c:
			_occ+=1
	return _occ

s = '01223334444abbccc'
print('%s contient %d occurrence(s) de %s' %(s, occurrence(s, '3'), '3'))
print('%s contient %d occurrence(s) de %s' %(s, s.count('4'), '4'))
