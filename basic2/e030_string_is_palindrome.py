while True:
	s = input('Entrez une chaîne de caractères : ')
	rs = s[::-1]
	if s == rs:
		print('c\'est un palindrome!')
		break
