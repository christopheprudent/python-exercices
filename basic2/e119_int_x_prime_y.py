# Create the gcd of two positive integers.
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

# https://www.cuemath.com/numbers/coprime-numbers/
def is_coprime(x, y):
    return gcd(x, y) == 1

print(is_coprime(17, 13))
print(is_coprime(17, 21))
print(is_coprime(15, 21))
print(is_coprime(25, 45))

