def insert_middle(s1, s2):
	pos = len(s1) // 2
	return s1[:pos] + s2 + s1[pos:]

print(insert_middle('[[]]', 'Python'))
print(insert_middle('{{}}', 'PHP'))
