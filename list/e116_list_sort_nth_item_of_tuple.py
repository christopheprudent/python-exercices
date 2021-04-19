def sort_nth_item_of_tuple(ll, nth):
    return sorted(ll, key=lambda x: x[nth])

# web solution
from operator import itemgetter
def index_on_inner_list(list_data, index_no):
    result = sorted(list_data, key=itemgetter(index_no))
    return result

L = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
print('liste', L)
print('triée sur élément {} : {}'.format(0, sort_nth_item_of_tuple(L, 0)))
print('triée sur élément {} : {}'.format(2, sort_nth_item_of_tuple(L, 2)))
print('triée sur élément {} : {}'.format(2, index_on_inner_list(L, 2)))
