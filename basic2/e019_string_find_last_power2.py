power2 = [ 2**x for x in range(21) ]
print(power2)

found = False
str2= input('Entrez une chaîne de puissances de 2 concanténées sans espace: ')
for i in range(20, 0, -1):
	str_p2 = str(power2[i])
	len_p2 = len(str_p2)
	print('Test %d: 2**%d=%s l=%d' %(i, i, str_p2, len_p2))
	if str2[-len_p2:] == str_p2:
		found = True
		print('dernière puissance de 2: ', i)
		break

if not found:
	print('pas trouvé, avec max puissance_2 égal à 20!')
