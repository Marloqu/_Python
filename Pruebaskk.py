n_valores = int(input("¿Cuántos valores quieres ordenar?"))

rango = range(n_valores)

print(rango)

print(n_valores)

print(type(rango))

print(type(n_valores))

lista = list()

print(lista)

for contador in rango:
    valor = 50 / (contador+1)
    lista.append(valor)

print(lista)

lista.sort()

print(lista)







