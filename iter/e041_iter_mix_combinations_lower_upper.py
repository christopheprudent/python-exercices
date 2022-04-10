# web solution
import itertools
def combination(str1):
    '''
    identifier minus/majus de chaque lettre de la chaîne à traiter, par exemple 'abc' ((c.lower(), c.upper()) for c in str1)
    [('a', 'A'), ('b', 'B'), ('c', 'C')]

    trouver les combinaisons (product)
    [('a', 'b', 'c'), ('a', 'b', 'C'), ('a', 'B', 'c'), ('a', 'B', 'C'), ('A', 'b', 'c'), ('A', 'b', 'C'), ('A', 'B', 'c'), ('A', 'B', 'C')]
    
    transformer en chaînes (map)
    ['abc', 'abC', 'aBc', 'aBC', 'Abc', 'AbC', 'ABc', 'ABC']
    '''
    result = map(''.join, itertools.product(*((c.lower(), c.upper()) for c in str1)))
    return list(result)

if __name__ == '__main__':
    st ="abc"
    print('donnée', st)
    print('ensemble des combinaisons (minus/majus)', combination(st))
    st ="w3r"
    print('donnée', st)
    print('ensemble des combinaisons (minus/majus)', combination(st))
    st ="Python"
    print('donnée', st)
    print('ensemble des combinaisons (minus/majus)', combination(st))
