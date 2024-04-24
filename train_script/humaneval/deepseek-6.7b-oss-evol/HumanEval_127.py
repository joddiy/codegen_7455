def intersection(interval1, interval2):
    # Check if the intervals intersect
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"

    # Calculate the intersection
    intersection_start = max(interval1[0], interval2[0])
    intersection_end = min(interval1[1], interval2[1])

    # Calculate the length of the intersection
    intersection_length = intersection_end - intersection_start + 1

    # Check if the length is a prime number
    if intersection_length < 2:
        return "NO"
    for i in range(2, int(intersection_length**0.5) + 1):
        if intersection_length % i == 0:
            return "NO"
    return "YES"

print(intersection((1, 2), (2, 3))) # ==> "NO"
print(intersection((-1, 1), (0, 4))) # ==> "NO"
print(intersection((-3, -1), (-5, 5))) # ==> "YES"