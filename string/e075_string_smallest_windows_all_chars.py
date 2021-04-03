
import collections

def all_subs(s):
	l = i = len(s)
	subs = []
	while i>0:
		subs += [ s[j:j+i] for j in range(l-i+1) ]
		#print(f'i={i} subs={subs}')
		i -= 1

	return subs

def smallest_windows_all_chars(s):
	print(f'chaîne minimale contenant tous les caractères de {s}')
	subs = sorted(all_subs(s), key=len)
	c = collections.Counter(s)
	chars = ''.join([ x for x in c.keys()])
	for sub in subs:
		if all(x in sub for x in chars):
			return sub
	return None

s = 'xswerabcdwd'
print(smallest_windows_all_chars(s))
s = 'asdaewsqgtwwsa'
print(smallest_windows_all_chars(s))
