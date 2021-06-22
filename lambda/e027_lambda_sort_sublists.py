L=[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
sort_list=lambda l : sorted(l)
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
result=[sort_list(x) for x in L]

print('liste', L)
print('sous-listes triées (lambda)')
print(result)

# web solution
# FIXME tri sur la première lettre de la couleur (et non le mot entier)!
def sort_sublists(input_list):
    #result = [sorted(x, key = lambda x:x[0]) for x in input_list] 
    result = [sorted(x) for x in input_list] 
    return result
print(sort_sublists(L))
