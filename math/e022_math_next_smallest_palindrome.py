def next_smallest_palindrome(n):
    _n = n
    while True:
        _str = str(_n)
        if _str == _str[::-1]:
            return _n

        _n += 1

if __name__ == '__main__':
    print('plus petit entier palindrome (suivant)')
    n = int(input('Entrer le nombre: '))
    palindrome = next_smallest_palindrome(n)
    print('dev) palindrome', palindrome)
