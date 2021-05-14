L = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
print('liste', L)
print('transformée en dictionnaire')
print(dict((x[0], x[1:]) for x in L))

# web solution
def test(lst):
    result = {item[0]: item[1:] for item in lst}
    return result

print(test(L))
