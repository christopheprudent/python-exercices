c=0
def f(x,y,z):
    if 0<=y<10 and 0<=z<10 and x[z][y]=='1':
        print('(i,j)=(%d,%d) %s' %(y, z, x[z]))
        x[z][y]='0'
        for dy,dz in [[-1,0],[1,0],[0,-1],[0,1]]:
            print('(di,dj)=(%d,%d)' %(dy, dz))
            f(x,y+dy,z+dz)

def print_data(x):
    print(''.join(map(lambda i: i.rjust(5, ' '), map(str, list(range(10))))))
    for i in range(10):
        print('%d %s' %(i, x[i]))

print("Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros") 
while 1:
    try:
        if c:input()
    except:break

    #x = [list(input()) for _ in [0]*10]
    x = [
      list('1100000111')
    , list('1000000111')
    , list('0000000111')
    , list('0010001000')
    , list('0000011100')
    , list('0000111110')
    , list('0001111111')
    , list('1000111110')
    , list('1100011100')
    , list('1110001000')
    ]

    print_data(x)
    #print('val(j=3): ', x[2])

    c=1
    b=0
    # j= ligne, i= colonne
    for i in range(10):
        for j in range(10):
            if x[j][i]=='1':
                print('x[%d][%d]=%s b=%d' %(j, i, x[j][i], b))
                b+=1
                f(x,i,j)
    print("Number of islands:")     
    print(b)

