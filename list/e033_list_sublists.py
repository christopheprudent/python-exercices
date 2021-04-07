# derived from string, but order is here not welcome!
def all_subs(s):
	l = i = len(s)
	subs = []
	while i>0:
		subs += [ s[j:j+i] for j in range(l-i+1) ]
		#print(f'i={i} subs={subs}')
		i -= 1

	return subs

from itertools import combinations
def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
		temp = [list(x) for x in combinations(my_list, i)]
		if len(temp)>0:
			subs.extend(temp)
	return subs

print(sub_lists([1,2,3,4]))
print(sub_lists(['X', 'Y', 'Z']))
