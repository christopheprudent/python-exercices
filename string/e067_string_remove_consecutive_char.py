def each_consecutive_char(s, c):
	i = 0
	occur = []
	each = []
	try:
		while i<len(s):
			i = s.index(c, i)
			#print(f'i={i}')
			j = i+1
			while j<len(s) and s[j] == c:
				j+=1
				#print(f'j={j}')
			occur.append(s[i:j])
			#print(f'i={i} j={j} occur={occur}')
			each.append((i, occur[-1]))
			i = j
	except ValueError:
		pass

	return each

print(each_consecutive_char("111000010000110", "0"))	

def remove_consecutive_char(s, c):
	s2 = ''
	i = 0
	for t in each_consecutive_char(s, c):
		print(f'i={i} s2={s2} t={t}')
		i += len(t[1])
		s2 += s[i:t[0]]

	print(f'i={i} s2={s2}')
	s2 += s[i]
	return s2

print(remove_consecutive_char("111000010000110", "0"))	
print(remove_consecutive_char("111000111", "0"))	
print(remove_consecutive_char("abc1aabbcc2aaabbbccc3", "c"))	
