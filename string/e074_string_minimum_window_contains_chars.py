def minimum_window_contains_chars(s, chars):
	b = e = -1
	found = []
	for i, c in enumerate(s):
		if c in chars:
			if not c in found:
				if len(found)==0:
					b = i
				found.append(c)

		if len(found)==len(chars):
			e = i+1
			break

	if b != -1 and e != -1:
		return s[b:e]
	else:
		return None

print(minimum_window_contains_chars("PRWSOERIUSFK", "OSU"))
