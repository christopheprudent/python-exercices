def filter_with_condition(l):
    return [x for x in l if not x%2 and x>45]

L = [12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
print('liste', L)
print('filtre (pair, > 45)', filter_with_condition(L))
