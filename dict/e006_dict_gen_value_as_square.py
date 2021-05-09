n=int(input("Saisissez un nombre entier: "))
print('génération dictionnaire (clé,valeur)=(i,i**2) pour les entiers [1..{}]'.format(n))
D = {}
for i in range(1, n+1):
    D[i] = i**2
print(D)
