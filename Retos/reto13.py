# FACTORIAL RECURSIVO
#  * Fecha publicación enunciado: 28/03/22
#  * Fecha publicación resolución: 04/04/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
#  *

def factorial(numero):  
    if numero == 0:
        return 1
    elif numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input("Número del que calcular el factorial: "))

print(f"El factorial del número {numero} es {factorial(numero)}")
