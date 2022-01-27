from e000_math_lib import proper_divisors

def is_abundant(n):
    return (sum(proper_divisors(n)) > n)

if __name__ == '__main__':
    print('dev) nombre abondant', 12, '?', is_abundant(12), proper_divisors(12))
    print('dev) nombre abondant', 13, '?', is_abundant(13), proper_divisors(13))

