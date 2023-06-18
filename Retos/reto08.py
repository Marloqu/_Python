""" DECIMAL A PRIMARIO """

# Dificultad: FÁCIL
#
# Enunciado: Crea un programa se encargue de transformar un número decimal a binario
# sin utilizar funciones propias del lenguaje que lo hagan directamente.

def entero_a_binario(entero):
    binario = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    resto = entero
    while resto != 0:
        for idx in range(10, -1, -1):
            if (resto / (2 ** idx)) >= 1:
                binario[idx] = 1
                resto = resto - (2 ** idx)
    return binario

numero_entero = int(input("Introduce un número entero positivo: "))

numero_binario = entero_a_binario(numero_entero)[::-1]

print(f"El número {numero_entero} se escribe así en formato binario: {numero_binario}")
