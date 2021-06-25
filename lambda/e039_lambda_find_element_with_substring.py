find_element_with_substring = lambda x, e : e in x

# web solution
def find_substring(str1, sub_str):
    result = list(filter(lambda x: sub_str in x, str1))
    return result

L = ['red', 'black', 'white', 'green', 'orange']
print('liste', L)
elem = 'ack'
print('éléments possédant la chaîne', elem)
print('mine:', [ x for x in L if find_element_with_substring(x, elem) ])
print(' web:', find_substring(L, elem))

elem = 'abc'
print('éléments possédant la chaîne', elem)
print('mine:', [ x for x in L if find_element_with_substring(x, elem) ])
print(' web:', find_substring(L, elem))
