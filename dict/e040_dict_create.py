D = dict()
D['x'] = list(range(11, 20))
D['y'] = list(range(21, 30))
D['z'] = list(range(31, 40))
print('dictionnaire', D)
print('accès 5e élément de chaque liste')
print(D['x'][4])
print(D['y'][4])
print(D['z'][4])
for k,v in D.items():
    print('clé {} a pour valeur {}'.format(k, v))

# web solution
D2 = dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40)))
import pprint
pprint.pprint(D2)
