# * Enunciado: Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

frase = input("Frase a dar la vuelta: ")
longitud = len(frase)
frase_vuelta = ""

for idx in range(longitud-1, -1, -1):
    frase_vuelta = frase_vuelta + frase[idx]
    print(frase_vuelta)


