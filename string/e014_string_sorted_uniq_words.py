words = input('Entrez plusieurs mots (séparés par une virgule) : ').split(',')
print('liste triée de mots uniques:', ','.join(sorted(set(words))))
