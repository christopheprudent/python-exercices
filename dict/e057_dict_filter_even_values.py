def filter_even_values(d):
    return dict((k, list(filter(lambda x:not x%2, v))) for k, v in d.items())

# web solution
def test(d):
    result = {key: [idx for idx in val if not idx % 2]  
          for key, val in d.items()}   
    return result 

D = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
print('dictionnaire', D)
print('filtre des valeurs paires uniquement')
print(filter_even_values(D))
print(test(D))

D = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
print('dictionnaire', D)
print('filtre des valeurs paires uniquement')
print(filter_even_values(D))
print(test(D))
