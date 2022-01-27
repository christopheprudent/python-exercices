# https://fr.wikipedia.org/wiki/Nombre_chanceux
def lucky_number(l, n, i=1):
    if i == n:
        return l
    else:
        _kth = 1 if i <= 2 else i-1;
        _l = [v for k, v in enumerate(l) if (k+1) % l[_kth]]
        print(f'i={i} : {_l} par élimination de chaque {l[_kth]}e élément')
        return lucky_number(_l, n, i+1)

if __name__ == '__main__':
    lucky = list(range(1, 101))
    print(f'i=0 : {lucky}')
    print('dev) nombres chanceux (n=10)', lucky_number(lucky, 10))

    # web solution
    n=int(input("Input a Number: "))
    List=range(-1,n*n+9,2)
    i=2
    while List[i:]:
        List=sorted(set(List)-set(List[List[i]::List[i]]))
        i+=1
    print(List[1:n+1])
