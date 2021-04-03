print('Entrez 2 valeurs entières (séparées par un espace):')
x, y = [int(x) for x in input().split()]
print('x=', x, 'y=', y)

x, y = map(int, input().split())
print('x=', x, 'y=', y)
