## https://stackoverflow.com/questions/15014310/why-is-there-no-xrange-function-in-python3
#def xrange(x,y,z):
#    return iter(range(x,y,z))
#
## https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
#
#def rwh_primes(n):
#    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
#    """ Returns  a list of primes < n """
#    sieve = [True] * n
#    for i in xrange(3,int(n**0.5)+1,2):
#        if sieve[i]:
#            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
#    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
#
#def sundaram3(max_n):
#    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/2073279#2073279
#    numbers = range(3, max_n+1, 2)
#    half = (max_n)//2
#    initial = 4
#
#    for step in xrange(3, max_n+1, 2):
#        for i in xrange(initial, half, step):
#            numbers[i-1] = 0
#        initial += 2*(step+1)
#
#        if initial > half:
#            return [2] + filter(None, numbers)
#
## https://fr.wikipedia.org/wiki/Indicatrice_d%27Euler
#def euler_phi(n):
#	primes = rwh_primes(n)
#	#primes = sundaram3(n)
#	print(primes)
#	return len(primes)
#
#print(euler_phi(10))
#print(euler_phi(15))
#print(euler_phi(33))

# web solution (w/ coprime!)

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        print(n)
        return len(n)
print(phi_func(10))
print(phi_func(15))
print(phi_func(33))

