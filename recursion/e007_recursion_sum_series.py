def sum_series(n):
    """
    sum = n+(n-2)+(n-4)... (until n-x =< 0)
    """
    if n -2 > 0:
        return n + sum_series(n -2)
    else:
        return 2

if __name__ == '__main__':
    print('dev) somme des valeurs de la série', 6, 'égale à', sum_series(6))
    print('dev) somme des valeurs de la série', 10, 'égale à', sum_series(10))
