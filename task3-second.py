def sieve_of_eratosthenes(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    primes = [num for num in range(2, N + 1) if is_prime[num]]

    return primes

N = 50
result = sieve_of_eratosthenes(N)
print(f"Простые числа до {N}: {result}")
