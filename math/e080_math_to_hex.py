def dec2base(n, b):
    if b > 36:
        return None
    if b == 10:
        return n

    _digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    _divs = []
    while True:
        _div = n // b
        _divs.append(_div)
        _rest = n - (_div * b)
        if _rest < b:
            break
        n = _rest

    #print(f'divs={_divs}')
    _t = ''
    for _i in _divs:
        _t += _digits[_i]
    _t += _digits[_rest]
    return '0X' + _t

def dec2hex(n):
    return dec2base(n, 16)


# https://stackoverflow.com/questions/5796238/python-convert-decimal-to-hex
def tohex(dec):
    x = (dec%16)
    digits = "0123456789ABCDEF"
    rest = int(dec/16)
    if (rest == 0):
        return digits[x]
    return tohex(rest) + digits[x]

if __name__ == '__main__':
    print('Conversion décimal en hexadécimal')
    n = int(input('Entrer un nombre entier (en base 10) : '))
    print('dev) conversion', n, 'égal à', dec2hex(n))
    print('web) conversion', n, 'égal à', format(n, '#04x'))

    numbers = [0,16,32,48,46,2,55,887]
    hex_ = ["0x"+tohex(i) for i in numbers]
    print('web) appel récursif', numbers, '->', hex_)
