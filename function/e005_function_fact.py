def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x-1)

print('calcul factoriel')
while True:
    n = int(input('entrez un nombre entier positif (0 pour arrêter) : ').strip())
    if n == 0:
        break
    print('%d! = %d' % (n, fact(n)))
