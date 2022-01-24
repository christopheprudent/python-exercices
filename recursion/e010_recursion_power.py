"""
élévation à la puissance: pow(x, n)

"""

def recursive_pow(x, n):
    if n > 1:
        return x * recursive_pow(x, n-1)
    else:
        return x

if __name__ == '__main__':
    print('dev) puissance x**n', 0, 2, 'égal à', recursive_pow(0, 2))
    print('dev) puissance x**n', -1, 2, 'égal à', recursive_pow(-1, 2))
    print('dev) puissance x**n', 3, 4, 'égal à', recursive_pow(3, 4))
    print('dev) puissance x**n', 4, 3, 'égal à', recursive_pow(4, 3))

