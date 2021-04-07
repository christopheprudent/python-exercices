def prime_eratosthenes(n):
    prime = []
    not_prime = []
    for i in range(2, n+1):
        if i not in not_prime:
            prime.append(i)
            for j in range(i*i, n+1, i):
                not_prime.append(j)
    return prime

print(prime_eratosthenes(30))

