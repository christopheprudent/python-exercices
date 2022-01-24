def factorial(x):
    if x > 1:
        return x * factorial(x -1)
    else:
        return 1

if __name__ == '__main__':
    print('dev) factoriel de', 1, 'égale à', factorial(1))
    print('dev) factoriel de', 10, 'égale à', factorial(10))
    print('dev) factoriel de', 100, 'égale à', factorial(100))
