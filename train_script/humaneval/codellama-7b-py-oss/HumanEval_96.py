def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    if n <= 1:
        return []

    primes = []
    for num in range(2, n):
        is_prime = True
        for divider in range(2, int(num ** 0.5) + 1):
            if num % divider == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes