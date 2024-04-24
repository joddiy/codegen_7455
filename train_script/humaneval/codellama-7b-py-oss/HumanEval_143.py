def words_in_sentence(sentence):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    result = [word for word in words if all(len(word) == i for i in range(2, len(word)) if is_prime(i))]
    return ' '.join(result)