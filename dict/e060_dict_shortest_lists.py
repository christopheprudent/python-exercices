def shortest_lists(d):
    _t = dict((k,len(v)) for k,v in d.items())
    _min = min(_t.values())
    return [k for k,v in _t.items() if v == _min]
    
# web solution (version améliorée)
def test(d):
    #min_value = 1
    min_value=min(map(len, d.values()))
    result = [k for k, v in d.items() if len(v) == min_value] 
    return result

D = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
print('dictionnaire', D)
print('ensemble des clés ayant la liste de taille minimale')
print(shortest_lists(D))
print(test(D))
