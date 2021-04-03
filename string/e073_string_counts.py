def counts(s):
	counts = [0] * 4;
	for c in s:
		if c.isupper():
			counts[0] += 1
		elif c.islower():
			counts[1] += 1
		elif not c.isalnum():
			counts[2] += 1
		elif c.isdigit():
			counts[3] += 1

	return tuple(counts)

print(counts("@W3Resource.Com"))
