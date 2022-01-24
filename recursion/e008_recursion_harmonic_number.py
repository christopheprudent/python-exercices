"""
Le terme général (un) de la série harmonique est défini par

{\displaystyle \forall n\in \mathbb {N} ^{*}\quad u_{n}={\frac {1}{n}}}{\displaystyle \forall n\in \mathbb {N} ^{*}\quad u_{n}={\frac {1}{n}}}.
On appelle n-ième nombre harmonique (noté classiquement Hn) la n-ième somme partielle de la série harmonique, qui est donc égale à

{\displaystyle H_{n}=1+{\frac {1}{2}}+{\frac {1}{3}}+{\frac {1}{4}}+\cdots +{\frac {1}{n}}=\sum _{k=1}^{n}{\frac {1}{k}}}{\displaystyle H_{n}=1+{\frac {1}{2}}+{\frac {1}{3}}+{\frac {1}{4}}+\cdots +{\frac {1}{n}}=\sum _{k=1}^{n}{\frac {1}{k}}}.
"""

def harmonic_number(n):
    if n > 1:
        return 1/n + harmonic_number(n-1)
    else:
        return 1

if __name__ == '__main__':
    print('dev) n-ième nombre harmonique', 4, 'égal à', harmonic_number(4))
    print('dev) n-ième nombre harmonique', 6, 'égal à', harmonic_number(6))
    print('dev) n-ième nombre harmonique', 7, 'égal à', harmonic_number(7))
    print('dev) n-ième nombre harmonique', 10, 'égal à', harmonic_number(10))

