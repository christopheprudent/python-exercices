import re

s = input('Entrez une chaîne codée, avec #<nb><caractère> pour dupliquer <caractère> <nb> fois, par ex: #3C pour CCC :')

while True:
	pound = s.find('#')
	if pound == -1:
		break
	else:
		m = re.search(r'([^#]*)#([0-9])([0-9A-Za-z-+\*/=_\.])(.*)', s)
		if m != None:
			for i in range(1, 5):
				print('m.group(%d)=%s' %(i, m.group(i)))
			s = m.group(1) + m.group(3) * int(m.group(2)) + m.group(4)

print('decoded string: ', s)
