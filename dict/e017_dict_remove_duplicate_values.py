# web solution
student_data = {
    'id1': {
        'name': ['Sara'], 
        'class': ['V'], 
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'], 
        'class': ['V'], 
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'], 
        'class': ['V'], 
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'], 
        'class': ['V'], 
        'subject_integration': ['english, math, science']
    },
}
print('dictionnaire, avec {} éléments'.format(len(student_data)))
print(student_data)

result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print('dictionnaire, après purge des valeurs en double, avec {} éléments'.format(len(result)))
print(result)
