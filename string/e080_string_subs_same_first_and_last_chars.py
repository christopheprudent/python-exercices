
import pprint

def all_subs(s):
	l = i = len(s)
	subs = []
	while i>0:
		subs += [ s[j:j+i] for j in range(l-i+1) ]
		#print(f'i={i} subs={subs}')
		i -= 1

	return subs

def subs_same_first_and_last_chars(s):
	subs = all_subs(s)
	ok = [ sub for sub in subs if sub[0] == sub[-1] ]
	return ok

s = input('Entrez une chaîne: ')
subs = subs_same_first_and_last_chars(s)
subs.insert(0, len(subs))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(subs)
