import bisect

# web solution
def index(a, x):
    """
    Le point d'insertion renvoyé, i, coupe la liste a en deux moitiés telles que
    pour la partie de gauche : all(val < x for val in a[lo:i])
    pour la partie de droite : all(val >= x for val in a[i:hi])
    """
    i = bisect.bisect_left(a, x)
    return i
    
a = [1,2,4,5]
print('liste', a)
print('index à gauche de {}'.format(6))
print(index(a, 6))
print('index à gauche de {}'.format(3))
print(index(a, 3))

