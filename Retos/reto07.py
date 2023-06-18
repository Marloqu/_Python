# * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre
# el recuento final de todas ellas.
# * - Los signos de puntuación no forman parte de la palabra.
# * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.

phrase = "Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev)."

phrase = phrase.replace(".", " ")
phrase = phrase.replace(",", " ")
phrase = phrase.replace("(", " ")
phrase = phrase.replace(")", " ")
phrase = phrase.casefold()


palabras_todas = phrase.split()

palabras_set = set(palabras_todas)

contador = 0

for idx in palabras_set:
    print(f"La palabra -{idx}- aparece {palabras_todas.count(idx)} veces en la frase")
    contador = contador + palabras_todas.count(idx)

print(f"La cantidad total de palabras que hay en la frase es {contador}")





