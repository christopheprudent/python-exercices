m = int(input('entrez le nombre de lignes : '))
n = int(input('entrez le nombre de colonnes : '))

M = []
for i in range(m):
    R = []
    for j in range(n):
        R.append(i*j)

    M.append(R)

print('Matrice: ', M)

# web solution
multi_list = [[0 for col in range(n)] for row in range(m)]

for row in range(m):
    for col in range(n):
        multi_list[row][col]= row*col

print('Matrice: ', multi_list)
