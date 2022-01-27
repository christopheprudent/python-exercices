# web solution
def amicable_numbers(limit):
    if not isinstance(limit, int):
        return "Input is not an integer!"

    if limit < 1:
        return "Input must be bigger than 0!"

    amicables = set()

    for num in range(2, limit+1):
        if num in amicables:
            continue

        sum_fact = sum([fact for fact in range(1, num) if num % fact == 0])
        sum_fact2 = sum([fact for fact in range(1, sum_fact) if sum_fact % fact == 0])
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact2)

    return amicables

if __name__ == '__main__':
    an = amicable_numbers(999)
    print('dev) nombres amicaux inférieurs à', 999, an, 'de somme: ', sum(an))

    an = amicable_numbers(9999)
    print('dev) nombres amicaux inférieurs à', 9999, an, 'de somme: ', sum(an))
