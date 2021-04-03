def print_matrix(mat):
	rows = len(mat)
	cols = len(mat[0])
	for i in range(rows):
		for j in range(cols):
			if (i+1) % 2:
				item = j
			else:
				item = cols - j -1

			print(mat[i][item])

matrix = [
	[1, 2, 3,4],
	[5, 6, 7, 8],
	[0, 6, 2, 8],
	[2, 3, 0, 2]
]

print_matrix(matrix)
