
def tr_s2(s):
	ns = s[:1]
	p = s[:1]
	for c in s[1:]:
		if c == p:
			continue

		p = c
		ns += c

	return ns

def tr_s(s):
	ns = s[:1]
	for c in s[1:]:
		if c == ns[-1]:
			continue

		ns += c

	return ns

# web solution
def no_consecutive_letters (txt):
    return txt[0] + ''.join(txt[i] for i in range(1,len(txt)) if txt[i] != txt[i-1])

print(tr_s("PPYYYTTHON"))
print(tr_s("PPyyythonnn"))
print(tr_s("Java"))
print(tr_s("PPPHHHPPP"))
