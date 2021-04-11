def sort_sublists(ll):
    r = list(map(sorted, ll))
    return sorted(r, key= lambda x: (len(x), x))

# web solution
def sort_sublists2(input_list):
    input_list.sort()  # sort by sublist contents
    input_list.sort(key=len)
    return input_list

L = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
print('liste de listes:', L)
print('liste des sous-listes triées par taille, valeur:', sort_sublists(L))

L = [[2], [0], [1, 3], [7, 0], [9, 11], [15, 13, 17]]
print('liste de listes:', L)
print('liste des sous-listes triées par taille, valeur:', sort_sublists(L))
