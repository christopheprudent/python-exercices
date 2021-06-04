import bisect

def index(a, x):
    """
    trouve la première occurence de x dans a (trié)
    """
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

# web solution
def index2(l, x): 
    i = bisect.bisect_left(l, x) 
    if i: 
        print(f'i={i}')
        return (i-1) 
    else: 
        return -1  

L = [1, 2, 3, 4, 8, 8, 10, 12]
print('liste', L)

while True:
    n = int(input('entrez élément: '))
    print('plus grand élément inférieur à {}'.format(n))

    try:
        i = index(L, n)
        if i > 0:
            print(L[i-1])
        else:
            print('pas de solution!')
    except ValueError:
        print('non trouvé!')

    i = index2(L, n)
    if i > -1:
        print(L[i])
    else:
        print('pas de solution!')
