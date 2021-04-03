def remove_characters_with_odd_index(s):
	t = [ c for i, c in enumerate(s) if not i % 2 ]
	return ''.join(t)

print(remove_characters_with_odd_index('a'))
print(remove_characters_with_odd_index('ab'))
print(remove_characters_with_odd_index('abc'))
print(remove_characters_with_odd_index('abcdefghijklmnopqrstuvwxyz'))
