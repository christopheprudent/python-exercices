m = 1
M = 22
print('nombres de {} à {}'.format(m, M))
N = range(m, M+1)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
S = map(str, N)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
divisible = lambda x : '0' not in x and all([int(x) % int(c) == 0 for c in x])
R = filter(divisible, S)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '12', '15', '22']
print('parmi ces nombres, seulement ceux divisibles par chacun de ses chiffres')
print(list(map(int, R)))

# web solution
def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num+1) \
            if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]

print(divisible_by_digits(m, M))
