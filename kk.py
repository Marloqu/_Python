# Vamos a ordenar 4 valores

# my_lista = list()

# my_lista.append(float(input("Valor 1: ")))
# my_lista.append(float(input("Valor 2: ")))
# my_lista.append(float(input("Valor 3: ")))
# my_lista.append(float(input("Valor 4: ")))

# my_lista.sort()

# print(my_lista)

a = 3
b = 2
c = 1

if a >= b:
    if a >= c:
        if b >= c:
            print("Éste es el orden correcto: ", a, b, c)
        else:
            print("Éste es el orden correcto: ", a, c, b)
    else:
        print("Éste es el orden correcto: ", c, a, b)
elif a >= c:
    print("Éste es el orden correcto: ", b, a, c)
elif b >= c:
    print("Éste es el orden correcto: ", b, c, a)
else:
    print("Éste es el orden correcto: ", c, b, a)


rango = range(1,2052,3)

# for contador in rango:
#    print(contador)

contador = 1

while contador <=10:
    print(contador)
    contador = contador +1

print("------------------------")

new_planet = ""

planets = list()

while new_planet.lower() != "done":
    if new_planet != "done" and new_planet != "":
        planets.append(new_planet)
    new_planet = input('Enter the name of a new planet, or done when done: ')

for contador in planets:
    print(contador)
    






