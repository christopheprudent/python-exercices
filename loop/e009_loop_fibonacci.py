def fibonacci(i):
    if i == 0 or i == 1:
        return i
    else:
        return fibonacci(i-2) + fibonacci(i-1)

# test
for i in range(10):
    print('{}: {}'.format(i, fibonacci(i)))

i = 0
while True:
    n = fibonacci(i)
    if n < 50:
        print(n, end=' ')
    else:
        break

    i += 1

print()
