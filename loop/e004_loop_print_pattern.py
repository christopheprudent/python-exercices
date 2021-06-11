N = 5

pattern = '* '
for i in range(1, N+1):
    print(pattern * i)
for i in range(N-1, 0, -1):
    print(pattern * i)
