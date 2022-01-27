# dev solution
"""
ABC A suivi des permutations de BC, soit ABC - A
    B                           AC
    C                           AB
"""

# web solution
def permute_string(str):
    """
    str='ABC'

    call permute_string BC
    call permute_string C
    call permute_string 
    str=C prev_list=['']
    next_list=['C']
    str=BC prev_list=['C']
    next_list=['BC', 'CB']
    str=ABC prev_list=['BC', 'CB']
    next_list=['ABC', 'BAC', 'BCA', 'ACB', 'CAB', 'CBA']
    """

    if len(str) == 0:
        return ['']
    print(f'call permute_string {str[1:]}')
    prev_list = permute_string(str[1:len(str)])
    print(f'str={str} prev_list={prev_list}')
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)

    print(f'next_list={next_list}')
    return next_list

if __name__ == '__main__':
    permutations = permute_string('ABC')
    print('web) liste permutations', 'ABC', permutations, 'avec: #', len(permutations), 'éléments')
    permutations = permute_string('ABCD')
    print('web) liste permutations', 'ABCD', permutations, 'avec: #', len(permutations), 'éléments')
