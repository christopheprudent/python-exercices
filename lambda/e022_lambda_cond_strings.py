sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']

# ['Dylan', 'Diana', 'Joanne']
t = [s for s in sample_names if not s[0].islower()]
t2 = list(filter(lambda s:not s[0].islower(), sample_names))

result = sum(map(len, filter(lambda s:not s[0].islower(), sample_names)))

print('ensemble de mots', sample_names)
print('somme des longueurs des mots, qui ne commencent pas par une minsucule : ', t2, 'soit', result)

# web solution
only_starts_not_lower=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
print(len(''.join(only_starts_not_lower)))
