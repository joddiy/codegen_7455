def largest_prime_sum(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    largest_prime = max(filter(is_prime, lst))
    return sum_of_digits(largest_prime)