def element_at_least_n_times(l, n, x):
    return len([i for i in l if i == n]) >= x

L = [0,1,3,5,0,3,4,5,0,8,0,3,6,0,3,1,1,0]
print('liste', L)
print('élément {} au moins présent {} fois : {}'.format(3, 4, element_at_least_n_times(L, 3, 4)))
print('élément {} au moins présent {} fois : {}'.format(0, 5, element_at_least_n_times(L, 0, 5)))
print('élément {} au moins présent {} fois : {}'.format(8, 3, element_at_least_n_times(L, 8, 3)))

# web solution
def check_element_in_list(lst, x, n):
    t = 0
    try:
        for _ in range(n):
            t = lst.index(x, t) + 1
        return True
    except ValueError:
        return False

print('élément {} au moins présent {} fois : {}'.format(3, 4, check_element_in_list(L, 3, 4)))
print('élément {} au moins présent {} fois : {}'.format(0, 5, check_element_in_list(L, 0, 5)))
print('élément {} au moins présent {} fois : {}'.format(8, 3, check_element_in_list(L, 8, 3)))
