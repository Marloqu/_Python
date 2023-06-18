#  * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.

def elimina_caracteres(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    out = ""
    for element in str1:
        if element not in str2:
            out += element
    print(out)

str1 = input("Primera cadena str1: ")
str2 = input("Segunda cadena str2: ")

elimina_caracteres(str1, str2)

elimina_caracteres(str2, str1)
