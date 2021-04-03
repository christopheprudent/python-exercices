okNumber = False
try:
	n = float(input('Entrez un nombre : '))
	okNumber = True
except (ValueError, TypeError):
	print('Vore saisie est incorrecte!')

if okNumber:
	print('Votre nombre saisi est', n)

