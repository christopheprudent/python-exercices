# https://www.geeksforgeeks.org/reduce-in-python/
# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

def multiply_elements(l):
    return functools.reduce(lambda a, b: a*b, l)
    
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('liste', list1)
print("le produuit de tous les éléments vaut : ", end="")
print(multiply_elements(list1))

list2 = [2.2, 4.12, 6.6, 8.1, 8.3]
print('liste', list2)
print("le produuit de tous les éléments vaut : ", end="")
print(multiply_elements(list2))
