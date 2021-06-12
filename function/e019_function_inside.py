# web solution
def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a+b
    return add

print('appel fonction imbriquée (sous-fonction)')
# a=2 b=4
func = test(2)
print(func(4))
