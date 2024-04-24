def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(6))
print(is_prime(101))
print(is_prime(11))
print(is_prime(13441))
print(is_prime(61))
print(is_prime(4))
print(is_prime(1))