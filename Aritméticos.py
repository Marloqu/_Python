seconds = 1042
display_minutes = seconds // 60
print(display_minutes)
display_seconds = seconds % 60
print(display_seconds)
print(17*60, display_seconds, 17*60+22)




first_planet = 149597870
second_planet = 778547200

distance_km = abs(first_planet - second_planet)

print(distance_km)

distance_mi = distance_km / 1.609344

print("La distancia en millas entre esos dos planetas es {}".format(distance_mi))

print("La distancia en millas entre esos dos planetas es %f" %(distance_mi))

print(f"La distancia en millas entre esos dos planetas es {distance_mi}")

print(f"La distnacia en km entre esos dos planetas es {distance_km}")

print(round(distance_mi))

from math import ceil, floor, pi # IMPORTACIÓN DE BIBLIOTECA MATH

round_up = ceil(12.5)
print(round_up)

print(pi)

round_down = floor(12.5)
print(round_down)





