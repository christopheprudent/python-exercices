"""
GCD greatest common divisor

"""

# https://www.mathematiquesfaciles.com/exercices/exercice-maths-2/exercice-maths-23038.php

def gcd(x, y):
    if x == y:
        return x 

    M = max(x, y)
    m = min(x, y)
    _mod = M % m
    return recursive_gcd(m, _mod)

def recursive_gcd(a, b):
    _mod = a % b
    if _mod > 0:
        return recursive_gcd(b, _mod)
    else:
        return b

# web solution
def Recurgcd(a, b):
	low = min(a, b)
	high = max(a, b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return Recurgcd(low, high%low)

if __name__ == '__main__':
    print('dev) PGCD', 561, 357, 'égal à', gcd(561, 357))
    print('web) PGCD', 561, 357, 'égal à', Recurgcd(561, 357))

