def capitalize_first_last(s):
	return s[0].upper() + s[1:-1] + s[-1].upper()

def capitalize_first_last_of_each_word(s):
	l = map(capitalize_first_last, s.split())
	return ' '.join(l)

print(capitalize_first_last_of_each_word("python exercises practice solution"))	
print(capitalize_first_last_of_each_word("w3resource"))	
