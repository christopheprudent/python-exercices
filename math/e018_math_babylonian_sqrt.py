# https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html
def BabylonianGuess(x):
    _str = str(x)
    _digits = len(_str) // 2
    _guess2 = 2* 10**(_digits-1)
    _guess7 = 7* 10**(_digits-1)
    if abs(_guess2 ** 2 -x) < abs(_guess7 ** 2 -x):
        return _guess2
    else:
        return _guess7

def BabylonianSqrt(x):
    epsilon = 10 ** (-2);
    if x < 0:
        _sqrt = None
    elif x == 0:
        _sqrt = 0
    else:
        _sqrt = BabylonianGuess(x)
        _sqrt_prev = 0
        # approximation à epsilon près
        while (abs(_sqrt - _sqrt_prev) > epsilon):
            _sqrt_prev = _sqrt
            # moyenne
            _sqrt = (_sqrt_prev + (x/_sqrt_prev)) / 2

    return _sqrt

# web solution
def BabylonianAlgorithm(number):
    if (number < 0):
        return None
    if(number == 0):
        return 0

    g = number/2.0
    g2 = g + 1
    while(g != g2):
        n = number/ g
        g2 = g;
        g = (g + n)/2

    return g

if __name__ == '__main__':
    import math
    numbers = [-3,0,1,2,4,10,16,30,100,3249,125348]
    for number in numbers:
        sqrt = BabylonianSqrt(number)
        print('dev) approximation racine carrée', number, 'égale à', sqrt)
        print('web) approximation racine carrée', number, 'égale à', BabylonianAlgorithm(number))
        if sqrt:
            print('     différence avec sqrt()', abs(math.sqrt(number) - sqrt))
