def get_nth_item_of_each_tuple(lt, nth):
    return [t[nth] for t in lt]

LT = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
print('liste', LT)
print('élément {} de chaque tuple: {}'.format(0, get_nth_item_of_each_tuple(LT, 0)))
print('élément {} de chaque tuple: {}'.format(2, get_nth_item_of_each_tuple(LT, 2)))
