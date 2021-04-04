# web solution
def mult_list(items):
    mult = 1
    for x in items:
        mult *= x
    return mult

l=[1,2,-8]
print(mult_list(l))
