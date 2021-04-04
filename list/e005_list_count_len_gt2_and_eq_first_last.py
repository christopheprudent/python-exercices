def items_len_gt2_and_eq_first_last(l):
	return [ x for x in l if len(x) > 2 and x[0] == x[-1] ]

l = ['abc', 'xyz', 'aba', '1221']
fl = items_len_gt2_and_eq_first_last(l)
print('liste={} filtrée={} avec #{} éléments'.format(l, fl, len(fl)))
