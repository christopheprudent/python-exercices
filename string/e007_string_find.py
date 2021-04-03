def find_and_replace_if(s):
	p1 = s.find('not')
	p2 = s.find('poor')

	if p1 > -1 and p2 > -1 and p1 < p2:
		# web solution
		# s = s.replace(s[p1:(p2+4)], 'good')
		return s[:p1] + 'good' + s[p2+4]
	else:
		return s

print(find_and_replace_if('The lyrics is not that poor!'))
print(find_and_replace_if('The lyrics is poor!'))
