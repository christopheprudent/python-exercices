"""
série géométrique est défini par: sum(1/pow(2, n))

"""

def geometric_sum(n):
    if n >= 0:
        return 1/pow(2, n) + geometric_sum(n-1)
    else:
        return 0

if __name__ == '__main__':
    print('dev) somme série géométrique 1/2**n', 4, 'égal à', geometric_sum(4))
    print('dev) somme série géométrique 1/2**n', 7, 'égal à', geometric_sum(7))

