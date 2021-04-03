import collections

def to_1st_uniq_2nd_multipe_chars(s):
	c = collections.Counter(s)
	#c1 = dict((k, v) for (k, v) in c.items() if v==1)
	#c2 = dict((k, v) for (k, v) in c.items() if v>1)
	l_one = [ k for k in c.keys() if c[k]==1 ]
	l_multiple = [ k for k in c.keys() if c[k]>1 ]

	return (''.join(l_one), ''.join(l_multiple))

print("aabbcceffgh")
print(to_1st_uniq_2nd_multipe_chars("aabbcceffgh"))

	
