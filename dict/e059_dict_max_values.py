import operator

def max_values(d, nmax):
    ds = sorted(d.items(), key=operator.itemgetter(1))
    #print(ds)
    #[('a', 5), ('h', 8), ('b', 14), ('e', 24), ('c', 32), ('d', 35), ('g', 57), ('f', 100), ('i', 100)]
    return [x[0] for x in ds][-nmax:][::-1]

# web solution
def test(d, N):
    result = sorted(d, key=d.get, reverse=True)[:N]
    return result

# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# intéressant...

D = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
print('dictionnaire', D)
n = int(input('Entrez le nombre de valeurs maximales, pour lesquelles afficher la clé: '))
print(max_values(D, n))
print(test(D, n))
