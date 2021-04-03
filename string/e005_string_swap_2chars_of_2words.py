str1, str2 = input('Entrez 2 mots séparés par un espace: ').split()
ns1 = str2[:2] + str1[2:]
ns2 = str1[:2] + str2[2:]

print(f'chaque mot (après échange des 2 premiers caractères de chacun): {ns1},{ns2}')
