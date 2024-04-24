def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            factors.append(i)

    if len(factors) == 3 and a == factors[0] * factors[1] * factors[2]:
        return True
    else:
        return False

print(is_multiply_prime(30))  # True