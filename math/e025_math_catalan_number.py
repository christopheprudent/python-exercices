# https://fr.wikipedia.org/wiki/Nombre_de_Catalan

from functools import reduce
def catalan_number(n):
    """
                  (2n)                         n
    Cn = 1 / (n+1)( n) = (2n)! / (n+1)!n! = PROD (n+k) / k pour n >= 0
                                             k=2
    """
    if n <= 1:
        return 1
    _catalan = [ (n+k)/k for k in range(2, n+1) ]
    return round(reduce((lambda x, y: x * y), _catalan))

    _cn = 1
    for _n in _catalan:
        _cn *= _n
    return _cn

# web solution
def catalan_number2(num):
    if num <=1:
         return 1
   
    res_num = 0
    for i in range(num):
        res_num += catalan_number2(i) * catalan_number2(num-i-1)
    return res_num

if __name__ == '__main__':
    n = int(input('Entrer un nombre entier : '))
    print('dev) nombre catalan', n, catalan_number(n))

    for n in range(10):
        print(catalan_number(n), catalan_number2(n))
