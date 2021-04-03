while True:
	n = int(input('Input number of rows/columns (0 to exit): '))
	if n == 0:
		break

	a = []
	for i in range(n):
		a.append([int(j) for j in input().split()])

	print(a)
	
	a.append([0] * (n+1))
	for i in range(n):
		a[i] += [sum(a[i])]
		for j in range(n+1):
			a[n][j] += a[i][j]

	for i in range(n+1):
		for j in range(n+1):
			print('{0:>5}'.format(a[i][j]), end="")
		print()
