def count_upper(s):
    count = 0
    vowels = 'AEIOU'
    for i in range(0, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count

print(count_upper('aBCdEf'))  # returns 1
print(count_upper('abcdefg'))  # returns 0
print(count_upper('dBBE'))  # returns 0