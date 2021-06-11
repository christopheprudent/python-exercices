for i in range(1, 51):
    if not i % 3 and i % 5:
        print('fizz')
    elif i % 3 and not i % 5: 
        print('buzz')
    elif not i % 3 and not i % 5: 
        print('fizzbuzz')
    else:
        print(i)
