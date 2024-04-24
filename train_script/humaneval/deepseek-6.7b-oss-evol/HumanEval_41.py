def car_race_collision(n: int) -> int:
    """
    The number of collisions in a car race is equal to the number of cars in the race.
    This is because each car in the race will collide with every other car in the race.
    Therefore, the number of collisions is n * (n - 1) / 2.
    """
    return n * (n - 1) // 2