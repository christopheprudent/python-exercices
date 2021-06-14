startwith = lambda s, p : s[0] == p;

# web solution
starts_with = lambda x: True if x.startswith('P') else False

S = 'Python'
print('chaîne', S)
print('commence par P : ', startwith(S, 'P'), starts_with(S))
S = 'C++'
print('chaîne', S)
print('commence par P : ', startwith(S, 'P'), starts_with(S))
