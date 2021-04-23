L = [10, 2, 56]
print('liste', L)
print('somme de chaque chiffre des entiers', sum(int(c) for x in map(str, L) if x.isdigit() for c in x))

L = [10, 20, 4, 5, 'b', 70, 'a']
print('liste', L)
print('somme de chaque chiffre des entiers', sum(int(c) for x in map(str, L) if x.isdigit() for c in x))

# FIXME ne prend pas en compte les entiers négatifs, sum=8 (au lieu de 19)
L = [10, 20, -4, 5, -70]
print('liste', L)
print('somme de chaque chiffre des entiers', sum(int(c) for x in map(str, L) if x.isdigit() for c in x))

# web solution
def sum_of_digits(nums):
    return sum(int(el) for n in nums for el in str(n) if el.isdigit())

print('somme de chaque chiffre des entiers', sum_of_digits(L))
