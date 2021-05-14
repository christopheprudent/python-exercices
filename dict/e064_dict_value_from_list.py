D = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
print('dictionnaire', D)
print('avec valeur prise dans la liste')
print({k:v[0] for k,v in D.items()})

# web solution
from itertools import product
def test(dic):
    # list(itertools.product(*dic.values()))
    # [('Jean Castro', 'Lula Powell', 'Brian Howell', 'Lynne Foster', 'Zachary Simon')]

    result = [dict(zip(dic, sub)) for sub in product(*dic.values())]
    # [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]
    return result

print(test(D))
