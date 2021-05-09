def remove_space(l):
    return list(map(str.strip, l))

# web solution
def test(lst):
    result =[]
    for i in lst:
        j = i.replace(' ','')
        result.append(j)
    return result

L = ['abc ', '  ', ' ', 'sdfds ', ' ', '     ', 'sdfds ', 'huy']
print('liste', L)
print('sans les espaces')
print(remove_space(L))
print(test(L))
