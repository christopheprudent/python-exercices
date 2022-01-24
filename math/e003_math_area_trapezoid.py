"""
A=(a+b)/2 x h
"""

def area_trapzoid(a, b, h):
    return ((a+b) / 2) * h

if __name__ == '__main__':
    print('dev) aire trapézoïde bases=', 5, 6, 'h=', 5, 'égal à', area_trapzoid(5, 6, 5))
