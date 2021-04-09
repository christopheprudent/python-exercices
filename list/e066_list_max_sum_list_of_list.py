def max_sum_list_of_list(ll):
    sl = [ (i, sum(l)) for i, l in enumerate(ll) ]
    return (max(sl, key= lambda x : x[1]))[0]

L = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print('liste de listes: ', L)
print('élément de plus grande somme: ', L[max_sum_list_of_list(L)])

# web solution
print(max(L, key=sum))
