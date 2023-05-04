loca = []
caca = ()
fea = {}

planet = {
    "Name": "Earth",
    "Moons": 1
}

print(planet.get("Name"))

print(planet["Name"])

planet.update({"Name": "Makemake"})
print(planet["Name"])

planet["Name"]= "Moreover"
print(planet["Name"])

planet.update({
              "Name": "Jupiter",
              "Moons": 79
})

print(planet["Name"], planet["Moons"])

planet["Orbital period"] =  4333

print(planet["Orbital period"])

print(planet)

planet.pop("Orbital period")

print(planet)

planet["Diameter (km)"] = {
    "Polar": 133709,
    "Equatorial": 142984
}

print(planet)


print("---------------------")



print(planet["Diameter (km)"]["Polar"])


print(planet.get(("Diameter (km)"), ("Polar")))

print("-------------PPPPPPPPPPPPPPPP--------")

planet = {
    "name": "Mars",
    "moons": 2
}

# print(f'The planet {planet["name"]} has {planet["moons"]} moon(s)')

print(f'The planet {planet["name"]}')



#planet.update('circumference (km)'{
#               "polar": 6752,
#               "equatorial": 6792
#               }
#)

print(planet)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

planet_moons = {
    "mercury": 0,
    "venus": 0,
    "earth": 1,
    "mars": 2,
    "jupiter": 79,
    "saturn": 82,
    "uranus": 27,
    "neptune": 14,
    "pluto": 5,
    "haumea": 2,
    "makemake": 1,
    "eris": 1
}

moons = planet_moons.values()

total_planets = len(planet_moons.keys())

print(moons)
print(type(moons))

print(total_planets)
print(type(total_planets))

total_moons = 0

for item in moons:
    total_moons = total_moons + item

print(total_moons)

print(total_moons / total_planets)























