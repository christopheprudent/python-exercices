import random
print(random.sample([i for i in range(1,100) if i%2==0], 10))

# alternative
print(random.sample(range(2,100,2), 10))


