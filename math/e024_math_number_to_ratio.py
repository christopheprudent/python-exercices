# https://unix.stackexchange.com/questions/581575/how-can-i-convert-a-float-to-ratio
"""
awk -v prec=0.001 -v max=2000 '
   function fract(n, k, kr, d){
       for(k=n;k<max;k+=n){
           kr=int(k+.5); d=kr-k; if(d<0)d=-d;
           if(d<prec){return kr"/"k/n}
       }
       return n" ??"
   }
   BEGIN{for(i=1;i<ARGC;i++)print fract(ARGV[i])}
' 3.1415926535 1.77777777 0.333333 2.71828 1.61803398
355/113
16/9
1/3
1264/465
987/610
"""

MAXNUMBER=5000

def convert_number_to_ratio(n, precision=0.001):
    k = n
    while k < MAXNUMBER:
        kr = int(k + .5)
        d = kr - k
        if d < 0:
            d = -d

        if d < precision:
            return str(kr) + "/" + str(int(k/n))

        k += n

if __name__ == '__main__':
    """
    dev) nombre 3.1415926535 converti en ratio 355/113
    dev) nombre 1.77777777 converti en ratio 16/9
    dev) nombre 0.333333 converti en ratio 1/3
    dev) nombre 2.71828 converti en ratio 1264/465
    dev) nombre 1.61803398 converti en ratio 987/609

    FIXME
    echo 'scale=8; 987/609' | bc
    1.62068965
    echo 'scale=8; 987/610' | bc
    1.61803278
    """
    from fractions import Fraction
    tests = [3.1415926535,1.77777777,0.333333,2.71828,1.61803398]
    for n in tests:
        print('dev) nombre', n, 'converti en ratio', convert_number_to_ratio(n))
        print('web) nombre', n, 'converti en ratio', Fraction(n).limit_denominator(MAXNUMBER), Fraction(n).limit_denominator())
