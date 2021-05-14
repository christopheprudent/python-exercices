# web solution
def test(dictt, key, value):
   if any(sub[key] == value for sub in dictt):
       return True
   return False

students = [
        {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
        {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
        {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
        {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
        {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]

print('dictionnaire', students)
print('test existence (clé, valeur)')

print('(clé, valeur)=(\'student_id\', 1)')
print(test(students,'student_id', 1))
print('(clé, valeur)=(\'name\', \'Brian Howell\')')
print(test(students,'name', 'Brian Howell'))
print('(clé, valeur)=(\'class\', \'VII\')')
print(test(students,'class', 'VII'))
print('(clé, valeur)=(\'class\', \'I\')')
print(test(students,'class', 'I'))
print('(clé, valeur)=(\'name\', \'Brian Howelll\')')
print(test(students,'name', 'Brian Howelll'))
print('(clé, valeur)=(\'student_id\', 11)')
print(test(students,'student_id', 11))
