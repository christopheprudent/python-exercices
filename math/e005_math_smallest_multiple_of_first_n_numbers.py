# web solution

def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    print('\n', factors)

    while True:
        for a in factors:
            print(f'facteur={a} i={i}')
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i
                
if __name__ == '__main__':
    print('web) plus petit multiple des', 2, 'premiers nombres égal à', smallest_multiple(2))
    print('web) plus petit multiple des', 5, 'premiers nombres égal à', smallest_multiple(5))
    #print('web) plus petit multiple des', 10, 'premiers nombres égal à', smallest_multiple(10))

