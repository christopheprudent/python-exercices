S = []

start = 1500
stop = 1700
for n in range(start, stop+1):
    if n % 5 == 0 and n %7 == 0:
        S.append(n)

print('nombres multiples de 5 et 7, compris entre {} et {}'.format(start, stop))
print(S)
