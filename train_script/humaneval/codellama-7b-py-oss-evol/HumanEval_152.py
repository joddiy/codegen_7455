def compare(game, guess):
    return [abs(g - s) for g, s in zip(guess, game)]

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # -> [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # -> [4,4,1,0,0,6]