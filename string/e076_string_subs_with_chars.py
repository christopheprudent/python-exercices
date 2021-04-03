
import collections

def all_subs(s):
	l = i = len(s)
	subs = []
	while i>0:
		subs += [ s[j:j+i] for j in range(l-i+1) ]
		#print(f'i={i} subs={subs}')
		i -= 1

	return subs

def subs_k_chars(s, k, chars):
	print(f'sous-chaînes de {s} contenant {k} fois les caractères de {chars}')
	subs = all_subs(s)
	ok = []
	for sub in subs:
		if all(sub.count(x) == k for x in chars):
			ok.append(sub)
	return ok

def subs_k_distinct_chars(s, k):
	print(f'sous-chaînes de {s} contenant {k} caractères distincts')
	subs = all_subs(s)
	ok = []
	for sub in subs:
		t = set(sub)
		if len(t) == k:
			ok.append(sub)
	return ok

s = input('Entrez une chaîne: ')
k = int(input('puis un nombre entier (de caractères distincts) : '))
print(subs_k_distinct_chars(s, k))
