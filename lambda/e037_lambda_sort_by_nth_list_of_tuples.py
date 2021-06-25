
# web solution

LT = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
print('liste de tuples', LT)
for i in range(1, len(LT[0])+1):
    print('liste triée selon le rang', i)
    print('mine: ', sorted(LT, key=lambda x:x[i-1]))
