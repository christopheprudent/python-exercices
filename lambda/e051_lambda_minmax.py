# web solution
def max_min_list_tuples(class_students):
    return_max = max(class_students, key=lambda item:item[1])[1]
    return_min = min(class_students, key=lambda item:item[1])[1]
    return return_max, return_min
    
class_students = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
print('liste de tuples', class_students)
print('trouver les éléments mix/max')
print(' web: (max, min)=', max_min_list_tuples(class_students))
