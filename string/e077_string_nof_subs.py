
import pprint

def all_subs(s):
	l = i = len(s)
	subs = []
	while i>0:
		subs += [ s[j:j+i] for j in range(l-i+1) ]
		#print(f'i={i} subs={subs}')
		i -= 1

	return subs

# web solution: n * (n+1) / 2 avec n = len(s)

s = input('Entrez une chaîne: ')
subs = all_subs(s)
subs.insert(0, len(subs))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(subs)
