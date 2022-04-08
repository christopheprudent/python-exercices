# web solution

def hamming(num):
    #Make a list of size n, n-1 is the value we want to return.
    h = [1] * num

    #Make 3 variables representing the 2^i, 3^j, 5^k of our hamming number.
    x2, x3, x5 = 2,3,5

    #Counter variables that we will raise 2, 3, and 5, to.
    i = j = k = 0

    print(f'(x2,x3,x5)=({x2},{x3},{x5}) (i,j,k)=({i},{j},{k}) h={h}')

    #Our initial list is filled with n values of the integer 1.
    for n in range(1, num):
        #Get the smallest number, then we will multiply it by 2, 3, or 5.
        h[n] = min(x2, x3, x5)
        print(f'n={n} h[{n}]={h[n]} (x2,x3,x5)=({x2},{x3},{x5})')
        if x2 == h[n]:
            i += 1
            x2 = 2 * h[i]
        if x3 == h[n]:
            j += 1
            x3 = 3 * h[j]
        if x5 == h[n]:
            k += 1
            x5 = 5 * h[k]

        print(f' (x2,x3,x5)=({x2},{x3},{x5}) (i,j,k)=({i},{j},{k}) h={h}')

    return h

# itertools, whaouh!
import itertools
from heapq import merge

def nth_hamming_number(n):
    def num_recur():
        last = 1
        yield last
        x, y, z = itertools.tee(num_recur(), 3)
        # fusion ordonnée des 3 itérables
        for n in merge((2 * i for i in x), (3 * i for i in y), (5 * i for i in z)):
            if n != last:
                yield n
                last = n
    result =  itertools.islice(num_recur(), n)
    return list(result)


if __name__ == '__main__':
    n = int(input('Entrez le rang des nombres réguliers à trouver: '))
    print()
    hn = hamming(n)
    print('\nnombres réguliers jusqu\'au rang %d: %s' % (n, hn))

    print()
    print(nth_hamming_number(8))
    print(nth_hamming_number(14))
    print(nth_hamming_number(17))

