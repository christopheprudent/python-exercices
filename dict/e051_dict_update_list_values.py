def update_list_values(d):
    for k,v in d.items():
        if k == 'Math':
            d[k] = list(map(lambda x:x+1, v))
        elif k == 'Physics':
            d[k] = list(map(lambda x:x-2, v))

D = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
print('dictionnaire', D)
print('après mises à jour: Math (+1), Physics (-2)')
update_list_values(D)
print(D)

# web solution
def test(dictionary):
    dictionary['Math'] = [x+1 for x in dictionary['Math']]
    dictionary['Physics'] = [x-2 for x in dictionary['Physics']]
    return dictionary

print(test(D))
