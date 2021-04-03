do_input = True
while True:
	if do_input:
		n = input('Entrez un nombre (0 pour terminer): ')
		if n == '0':
			break
		memo = []
		do_input = False
		n2 = n
	
	sum = 0
	for digit in n:
		d = int(digit)
		sum += d*d

	if sum in memo:
		print(f'{n2} n\'est pas happy!')
		do_input = True
	else:
		if sum == 1:
			print(f'{n2} est un nombre happy')
			do_input = True
		else:
			memo.append(sum)
			n = str(sum)
