d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50,6:60}

dall = {}
for d in (d1, d2, d3):
  dall.update(d)

print('dictionnaire1', d1)
print('dictionnaire2', d2)
print('dictionnaire3', d3)
print('concaténation de ces dictionnaires')
print(dall)
