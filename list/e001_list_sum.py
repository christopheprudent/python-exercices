# web solution
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

l=[1,2,-8]
print(sum_list(l))
print(sum(l))
