def list_divisors(n):
    _div = [1]
    for i in range(2, (n//2) +1):
        if not n % i:
            _div.append(i)

    return _div

print('savoir si un noimbre est un nombre parfait (à savoir s\'il est égal à la somme de ses diviseurs')
while True:
    n = int(input('entrez un nombre entier positif : ').strip())
    if n == 0:
        break

    divisors = list_divisors(n)
    print(' ses diviseurs sont: ', divisors)
    if n == sum(divisors):
        print(' %d est un nombre parfait!' % n)
    else:
        print(' retentez votre chance...')
