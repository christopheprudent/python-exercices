import collections
print('2e moins bonne note à trouver')

n = int(input('entrez le nombre d\'étudiants : '))
students = []
for i in range(n):
    _name = input('entrez son nom : ')
    _grade = float(input('entrez sa note : '))
    students.append([_name, _grade])

for i in range(n):
    print(students[i], end=" ")
print()

d = collections.defaultdict(list)
for i in range(n):
    d[students[i][1]].append(students[i][0])

print('répartition par note')
ds = sorted(d.items(), key=lambda x : x[0])
print(ds)

for i, t in enumerate(ds):
    if i == 0:
        _info_note = 'la moins bonne'
    else:
        _info_note = 'la ' + str(i+1) + 'e'
        

    print('avec {} note ({}) pour les étudiants {}'.format(_info_note, t[0], t[1]))

# web solution
order =sorted(students, key = lambda x: int(x[1]))
for i in range(n):
   if order[i][1] != order[0][1]:
       second_low = order[i][1]
       break
print('2e note la moins bonne: ', second_low)
sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()
print("\nEtudiants:")
for s_name in sec_student_name:
   print(s_name)
