# https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne

def sieveEratosthene(n):
    """
    Fonction Eratosthène(Limite)
        L = tableau de booléen de taille Limite, initialisé à Vrai
        L[1] = Faux
        Pour i de 2 à Limite
            Si L[i]
                Pour j de i*i à Limite par pas de i
                on peut commencer à i*i car tous les multiples de i inférieurs à i*i ont déjà été rayés
                    L[j] = Faux
                Fin pour
            Fin si
        Fin pour
        Retourner L
    Fin fonction
    """

    Eratosthene = [ True for _ in range(n+1) ]
    Eratosthene[0] = False
    Eratosthene[1] = False

    #for k, v in enumerate(Eratosthene):
    #    print(f'k={k} v={v}')

    for i in range(2, n+1):
        #print(f'i={i} {Eratosthene[i]}')
        if Eratosthene[i]:
            for j in range(i*i, n+1, i):
                Eratosthene[j] = False
    
    #print('\n')
    #for k, v in enumerate(Eratosthene):
    #    print(f'k={k} v={v}')

    return Eratosthene

# web solution
def sieve_of_Eratosthenes(num):
    limitn = num+1
    not_prime_num = set()
    prime_nums = []

    for i in range(2, limitn):
        if i in not_prime_num:
            continue

        for f in range(i*2, limitn, i):
            not_prime_num.add(f)

        prime_nums.append(i)

    return prime_nums

if __name__ == '__main__':
    print('crible Eratosthène')
    n = int(input('Entrer la limite désirée: '))
    output = 0
    Eratosthene = sieveEratosthene(n)
    print('dev) crible Eratosthène', Eratosthene)
    #print('\n')
    #for k, v in enumerate(Eratosthene):
    #    print(f'k={k} v={v}')
    for k, v in enumerate(Eratosthene):
        if v:
            print('%3d' % k, end=' ')
            output += 1
        if output == 10:
            print()
            output = 0
    
    print('\n')

    Eratosthene2 = sieve_of_Eratosthenes(n)
    print('web) crible Eratosthène', Eratosthene2)
