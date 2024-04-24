def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics)."""
    return pow(2, n, p)