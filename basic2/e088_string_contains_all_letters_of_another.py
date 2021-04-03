def all_letters_in(s, in_s):
	_s = set(s)
	return set(in_s).issubset(_s)

print(all_letters_in("python", "ypth"))
print(all_letters_in("python", "ypths"))
print(all_letters_in("python", "ypthon"))
print(all_letters_in("123456", "01234"))
print(all_letters_in("123456", "1234"))
	
