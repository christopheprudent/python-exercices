colors = ["Red", "Green", "Black", "Orange"]
print('liste de chaînes')
print(colors)
print('convertie en liste de listes')
# [['R', 'e', 'd'], ['G', 'r', 'e', 'e', 'n'], ['B', 'l', 'a', 'c', 'k'], ['O', 'r', 'a', 'n', 'g', 'e']]
print(list(map(list, colors)))
