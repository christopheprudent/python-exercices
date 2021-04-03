def max_consecutive_char(s, c):
	i = 0
	occur = []
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
			i = j
	except ValueError:
		pass

	return max(map(len, occur))

print(max_consecutive_char("111000010000110", "0"))	
print(max_consecutive_char("111000111", "0"))	
print(max_consecutive_char("abc1aabbcc2aaabbbccc3", "c"))	
