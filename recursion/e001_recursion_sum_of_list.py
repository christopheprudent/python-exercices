def recursion_sum_of_list(list, i=0):
    if i == len(list):
        return 0
    else:
        return list[i] + recursion_sum_of_list(list, i+1)

# web solution
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])

def sumDigits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits(int(n / 10))

if __name__ == '__main__':
    tests = [1, 5, -2, 60, 15]
    print('dev) somme des valeurs de', tests, 'égale à', recursion_sum_of_list(tests))
    print('web) somme des valeurs de', tests, 'égale à', list_sum(tests))

    i = 345
    l = list(map(int, str(i)))
    print('dev) somme des chiffres de', i, 'égale à', recursion_sum_of_list(l))
    print('web) somme des chiffres de', i, 'égale à', sumDigits(i))
    i = 45
    l = list(map(int, str(i)))
    print('dev) somme des chiffres de', i, 'égale à', recursion_sum_of_list(l))
    print('web) somme des chiffres de', i, 'égale à', sumDigits(i))
    
