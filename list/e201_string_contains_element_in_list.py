def str_contains_element_in_list(s, l):
    return any(x in s for x in l)

# web solution
def test(lst,str1):
    result = [el for el in lst if(el in str1)] 
    return bool(result)

S = 'https://www.w3resource.com/python-exercises/list'
L = ['.com', '.edu', '.tv']
print('chaîne', S)
print('liste', L)
print('avec au moins un élément de la liste')
print(str_contains_element_in_list(S, L))
print(test(L, S))

S = 'https://www.w3resource.net'
L = ['.com', '.edu', '.tv']
print('chaîne', S)
print('liste', L)
print('avec au moins un élément de la liste')
print(str_contains_element_in_list(S, L))
print(test(L, S))
