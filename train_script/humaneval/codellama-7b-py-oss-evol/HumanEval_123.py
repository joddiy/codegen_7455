def get_odd_collatz(n):
    def collatz(n):
        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            sequence.append(n)
        return sequence

    odd_numbers = [n for n in collatz(n) if n % 2 != 0]
    return sorted(odd_numbers)

print(get_odd_collatz(5))  # Output: [1, 5]