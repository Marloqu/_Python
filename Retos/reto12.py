#  * ¿ES UN PALÍNDROMO?
#  * Fecha publicación enunciado: 21/03/22
#  * Fecha publicación resolución: 28/03/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.

def es_palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto_inverse = texto[::-1]
    if texto == texto_inverse:
        si_o_no = True
    else:
        si_o_no = False
    return si_o_no

texto = input("Texto a comprobar si es o no palíndromo: ")

si_o_no = es_palindromo(texto)

print(f"¿El texto {texto} es palíndromo?: {si_o_no}")