def bf(planet1, planet2):
    planet_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        planet1_index = planet_order.index(planet1)
        planet2_index = planet_order.index(planet2)
        if planet1_index > planet2_index:
            planet1_index, planet2_index = planet2_index, planet1_index
        return tuple(planet_order[planet1_index+1:planet2_index])
    except ValueError:
        return ()

print(bf("Jupiter", "Neptune")) # ==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury")) # ==> ("Venus")
print(bf("Mercury", "Uranus")) # ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")