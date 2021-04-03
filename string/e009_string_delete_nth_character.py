def delete_nth_character(s, n):
	if n > 0 and len(s) >= n:
		s = s[:n-1] + s[n:]

	return s

print(delete_nth_character('abcdef', 1))
print(delete_nth_character('abcdef', 3))
print(delete_nth_character('abcdef', 6))
