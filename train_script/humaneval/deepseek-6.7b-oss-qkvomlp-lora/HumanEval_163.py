def generate_integers(a, b):
    a, b = min(a, b), max(a, b)  # Ensure a is the smaller number
    return [i for i in range(a, b+1) if i % 2 == 0]