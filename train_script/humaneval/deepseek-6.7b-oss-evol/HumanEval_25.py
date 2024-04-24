from typing import List


def factorize(n: int) -> List[int]:
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor:
            divisor += 1
        else:
            n //= divisor
            factors.append(divisor)
    if n > 1:
        factors.append(n)
    return factors