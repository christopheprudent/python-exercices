def all_has_same_value(d, value):
    return all(d[k] == value for k in d.keys())

# web solution
def value_check(students, n):
    result = all(x == n for x in students.values()) 
    return result

D = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
print('dictionnaire', D)
print('tous les éléments sont égaux à {} : {}, {}'.format(12, all_has_same_value(D, 12), value_check(D, 12)))
print('tous les éléments sont égaux à {} : {}, {}'.format(10, all_has_same_value(D, 10), value_check(D, 10)))
