# /*
#  * Reto #16
#  * EN MAYÚSCULA
#  * Fecha publicación enunciado: 18/04/22
#  * Fecha publicación resolución: 25/04/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
#  * poner en mayúscula la primera letra de cada palabra.
#  * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

# Crea un diccionario con el alfabeto en minúsculas en clave, y en mayúsculas en valor

import string
clave = string.ascii_lowercase
valor = string.ascii_uppercase
matriz = dict(zip(clave,valor))

# Añado la ñ y Ñ

matriz["ñ"] = "Ñ"

def modo_titulo(cadena):
    cadena = list(cadena)
    for idx in range(len(cadena)):
        if idx == 0 and (cadena[idx] in matriz):
            cadena[idx] = matriz[cadena[idx]]
        elif (cadena[idx] in matriz) and (cadena[idx - 1] == " "):
            cadena[idx] = matriz[cadena[idx]]
    salida = ""
    for element in cadena:
        salida += element
    return salida

cadena = input("Cadena a poner en modo título: ")

print(f"La cadena \"{cadena}\" en formato título se escribe así: \"{modo_titulo(cadena)}\"")