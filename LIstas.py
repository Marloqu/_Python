planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

planets2 = planets*2

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

print("The last planet is", planets[-1])
print("The planet before the last one is", planets[-2])

planets[3] = "Cacadelavaca"
print(planets[3])

print(len(planets))

planets[6] = planets2


print(len(planets2))

print(planets2)

print(planets[6])

print(planets.pop(6))

print("-----------------------------------")


planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print(planets)

print("There are", len(planets), "planets")

planets.append("Pluto")
print(planets[-1], "has been added to the list")
print("There are", len(planets), "planets")
print(planets[-1])

print(min(planets))
print(max(planets))
print(planets)

planets_before_earth = planets[0:2]
print(planets_before_earth)

planets_after_earth = planets[3:8]
print(planets_after_earth)

planets_after_earth = planets[3:]
print(planets_after_earth)

planets_prueba = planets[:]
print(planets_prueba)

planets_prueba = planets
print(planets_prueba)

planets_prueba = planets[1::-1]
print(planets_prueba)

planets.sort()

print(planets)
print(type(planets))

planets_after_earth = planets[3:]
print(planets_after_earth)

print("-----------------------------------")


# my_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rango = range(1,21,1)

my_lista = list()

for contador in rango:
    valor = contador
    my_lista.append(valor)

print(my_lista)

print(my_lista[:3:-1])






planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

user_planet = input("Please enter the name of the planet (with a capital letter to start)")

planet_index = planets.index(user_planet)

planets_closer_to_the_sun = planets [:planet_index]

print(f"These are the planets closer than {user_planet} to the sun: {planets_closer_to_the_sun}")

planets_further_from_sun = planets [planet_index + 1:]

print(f"These are the planets further from sun apart than {user_planet}: {planets_further_from_sun}")







