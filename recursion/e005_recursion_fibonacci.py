def fibonacci(n):
    f0 = 0
    f1 = 1
    if n >= 2:
        return fibonacci(n-1) + fibonacci(n-2)
    elif n == 1:
        return f1
    else:
        return f0


if __name__ == '__main__':
    print('dev) élément suite Fibonacci de rang', 0, 'égale à', fibonacci(0))
    print('dev) élément suite Fibonacci de rang', 1, 'égale à', fibonacci(1))
    print('dev) élément suite Fibonacci de rang', 10, 'égale à', fibonacci(10))
