L = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
iL = list(map(round, L))
m = min(iL)
M = max(iL)
iL5 = sorted(map(lambda x: x*5, iL))

print('liste', L)
print('éléments arrondis :', iL)
print(f'min={m} max={M}')
print('éléments *5, triés par ordre croissant:', ' '.join(map(str, iL5)))
