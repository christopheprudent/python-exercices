import random

def get_random_except(L, Ex):
    L2=list(set(L).difference(Ex))
    return random.choice(L2)

L=list(range(1,11))
print('liste', L)
print('élément aléatoire : {} parmi liste, excepté {}'.format(get_random_except(L, [2, 9, 10]), [2, 9, 10]))

L2=list(range(-5, 6))
print('liste', L2)
print('élément aléatoire : {} parmi liste, excepté {}'.format(get_random_except(L2, [-5, 0, 4, 3, 2]), [-5, 0, 4, 3, 2]))

# web solution
def generate_random(start_range, end_range, nums):
    result = random.choice([i for i in range(start_range,end_range) if i not in nums])
    return result

start_range = 1
end_range = 10
nums = [2, 9, 10]
print("\nGenerate a number in a specified range (1, 10) except [2, 9, 10]")
print(generate_random(start_range,end_range,nums))
