def eat(number, need, remaining):
    # Calculate the total number of carrots that can be eaten
    total_eaten = number + min(need, remaining)
    # Calculate the number of carrots left after the meals
    carrots_left = max(0, remaining - need)
    return [total_eaten, carrots_left]