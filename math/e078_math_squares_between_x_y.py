# web solution
def squares(a, b):
    lists=[]
    # Traverse through all numbers
    for i in range (a,b+1):
        print(f'i={i}')
        j = 1;
        print(' j=', end='')
        while j*j <= i:
            _end = ' '
            if j*j == i:
                _end = 'c'
                lists.append(i)
            print(f'{j}', end=_end)
            j = j+1
        print()
        #i = i+1
    return lists

print('liste carrès entre 2 nombres')
sq = squares(1, 30)
print(sq)
