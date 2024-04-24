def compare(game, guess):
    return [abs(g - x) for x, g in zip(game, guess)]