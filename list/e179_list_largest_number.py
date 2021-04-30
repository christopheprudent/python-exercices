def largest_number(l):
    return ''.join(sorted(map(str, l), reverse=True))

# web solution
def create_largest_number(lst):
    if all(val == 0 for val in lst):
        return '0'
    result = ''.join(sorted((str(val) for val in lst), reverse=True,
                      key=lambda i: i*( len(str(min(lst))) * 2 // len(i))))
    return result

L = [3, 40, 41, 43, 74, 9]
print('liste', L)
print('trié pour obtenir le plus grand nombre', largest_number(L), create_largest_number(L))

L = [10, 40, 20, 30, 50, 60]
print('liste', L)
print('trié pour obtenir le plus grand nombre', largest_number(L))

L = [8, 4, 2, 9, 5, 6, 1, 0]
print('liste', L)
print('trié pour obtenir le plus grand nombre', largest_number(L))
