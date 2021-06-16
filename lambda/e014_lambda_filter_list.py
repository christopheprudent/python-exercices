L = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print('liste', L)
print('seulement les éléments de taille 6')
print(list(filter(lambda x: len(x) == 6, L)))
