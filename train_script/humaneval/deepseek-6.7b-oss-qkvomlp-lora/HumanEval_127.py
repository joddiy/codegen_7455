def intersection(interval1, interval2):
    # Check if the intervals intersect
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"
    
    # Calculate the intersection
    intersection_start = max(interval1[0], interval2[0])
    intersection_end = min(interval1[1], interval2[1])
    
    # Calculate the length of the intersection
    intersection_length = intersection_end - intersection_start + 1
    
    # Check if the length of the intersection is a prime number
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True