s = 'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
print('chaîne avec un mélange de nombres et alpha')
n = s.split()
# seulement les nombres
n2 = [x for x in n if x.isdigit()]
# seulement les nombres, plus grand que le nombre de nombres!
result = list(sorted(filter(lambda x : int(x) > len(n2), n2)))
print('seulement les nombres (plus grand que le nombre de nombres!)', result)
