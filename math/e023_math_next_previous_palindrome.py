def next_previous_palindrome(n):
    _n = n
    while True:
        _str = str(_n)
        if _str == _str[::-1]:
            return _n

        _n -= 1

        if _n == 0:
            return None

if __name__ == '__main__':
    print('plus petit entier palindrome (précédent)')
    n = int(input('Entrer le nombre: '))
    palindrome = next_previous_palindrome(n)
    print('dev) palindrome', palindrome)
