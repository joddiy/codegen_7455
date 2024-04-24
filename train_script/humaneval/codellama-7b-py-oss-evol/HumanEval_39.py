def is_prime(n: int) -> bool:
    """
    is_prime checks if a number is prime.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_fibonacci(n: int) -> bool:
    """
    is_fibonacci checks if a number is a Fibonacci number.
    """
    x = 0
    y = 1
    while y < n:
        z = x + y
        x = y
        y = z
    return y == n

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    i = 0
    count = 0
    while count < n:
        if is_prime(i) and is_fibonacci(i):
            count += 1
        i += 1
    return i - 1