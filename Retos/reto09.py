# * Dificultad: MEDIA
# *
# * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios
# entre palabras "  ".
# * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

# Define dict from natural to morse

natural_morse = {
    " ": "  ",
    "A": ".- ",
    "B": "-...",
    "C": "-.-. ",
    "CH": "---- ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "Ñ": "--.-- ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- "
    }

# Invert k / v from previous dict and get morse to natural

morse_natural = {v: k for k, v in natural_morse.items()}

def natural_a_morse(texto):
    morse = []
    for element in texto:
        morse += natural_morse[element]
    return morse

def morse_a_natural(texto):
    natural = []
    texto = texto.split()
    for element in texto:
        natural += morse_natural[element + " "]
    return natural

texto = input("¿Qué mensaje quieres transformar?")

if texto[0] == "." or texto[0] == "-":
    natural = morse_a_natural(texto)
    for element in natural:
        print(element, end = "")
else:
    morse = natural_a_morse(texto.upper())
    for element in morse:
        print(element, end = "")


