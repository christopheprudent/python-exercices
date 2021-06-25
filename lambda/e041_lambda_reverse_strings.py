reverse_str = lambda s : s[::-1]

# web solution
def reverse_strings_list(string_list):
    result = list(map(lambda x: "".join(reversed(x)), string_list))
    return result

L = ['Red', 'Green', 'Blue', 'White', 'Black']
print('liste', L)
print('inversion des chaînes')
print('mine:', list(map(reverse_str, L)))
print(' web:', reverse_strings_list(L))
