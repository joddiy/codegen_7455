def skjkasdkd(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    max_prime = max(lst)
    while not is_prime(max_prime):
        lst.remove(max_prime)
        max_prime = max(lst)

    return sum_of_digits(max_prime)