def count_up_to(n):
    if n <= 1:
        return []
    primes = [2]
    for i in range(3, n):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes