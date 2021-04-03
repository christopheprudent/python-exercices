value = input('Entrez une valeur numérique entière: ')
times = int(input('Entrez le nombre de réplication, à sommer : '))

_sum = 0
for i in range(1, times+1):
	_sum += int(value * i)
	#print(i, _sum)

print('La somme des %i réplications de la valeur %s est égale à %i' %(times, value, _sum))
