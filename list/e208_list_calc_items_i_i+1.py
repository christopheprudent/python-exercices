def calc_adjacents_items(l):
    return [(x+y)/2 for x,y in zip(l, l[1:])]

L = [1, 2, 3, 4, 5, 6, 7]
print('liste', L)
print('après calcul (élément(i) + élément(i+1))/2')
print(calc_adjacents_items(L))

L = [0, 1, -3, 3, 7, -5, 6, 7, 11]
print('liste', L)
print('après calcul (élément(i) + élément(i+1))/2')
print(calc_adjacents_items(L))
