L=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print('liste de listes', L)

max_list= lambda X : max(len(x) for x in X)
min_list= lambda X : min(len(x) for x in X)

# [(3, [13, 15, 17])]
print('sous-liste avec le maximum d\'éléments', [(len(x), x) for x in L if len(x) == max_list(L)])
# [(1, [0])]
print('sous-liste avec le minimum d\'éléments', [(len(x), x) for x in L if len(x) == min_list(L)])

# web solution
def max_length_list(input_list):
    max_length = max(len(x) for x in input_list )   
    max_list = max(input_list, key = lambda i: len(i))    
    return(max_length, max_list)
    
def min_length_list(input_list):
    min_length = min(len(x) for x in input_list )  
    min_list = min(input_list, key = lambda i: len(i))
    return(min_length, min_list)

print('sous-liste avec le maximum d\'éléments', max_length_list(L))
print('sous-liste avec le minimum d\'éléments', min_length_list(L))
