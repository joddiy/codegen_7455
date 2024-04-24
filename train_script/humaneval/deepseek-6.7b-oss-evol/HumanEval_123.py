def get_odd_collatz(n):
    def collatz(n):
        result = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            result.append(n)
        return result

    collatz_sequence = collatz(n)
    odd_numbers = [num for num in collatz_sequence if num % 2 != 0]
    return sorted(list(set(odd_numbers)))