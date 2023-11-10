def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(start, end):
    twin_primes = []
    for i in range(start, end - 1):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes

start_range = 10
end_range = 50

result = find_twin_primes(start_range, end_range)
print(f"Простые числа-близнецы в диапазоне от {start_range} до {end_range}:")
for twin_prime_pair in result:
    print(twin_prime_pair)
