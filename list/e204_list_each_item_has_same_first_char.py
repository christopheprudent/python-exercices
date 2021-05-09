def each_item_has_same_first_char(l):
    ls = list(map(str, l))
    return all(s[0] == ls[0][0] for s in ls)

# web solution
def test(lst):
    result = all(str(x)[0] == str(lst[0])[0] for x in lst) 
    return result

L = [1234, 122, 1984, 19372, 100]
print('liste', L)
print('tous les éléments commencent par la même valeur')
print(each_item_has_same_first_char(L))

L = [1234, 922, 1984, 19372, 100]
print('liste', L)
print('tous les éléments commencent par la même valeur')
print(each_item_has_same_first_char(L))

L = ['aabc', 'abc', 'ab', 'a']
print('liste', L)
print('tous les éléments commencent par la même valeur')
print(each_item_has_same_first_char(L))

L = ['aabc', 'abc', 'ab', 'ha']
print('liste', L)
print('tous les éléments commencent par la même valeur')
print(each_item_has_same_first_char(L))
