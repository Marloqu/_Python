# /*
#  * Reto #17
#  * LA CARRERA DE OBSTÁCULOS
#  * Fecha publicación enunciado: 25/04/22
#  * Fecha publicación resolución: 02/05/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
#  * carrera de obstáculos.
#  * - La función recibirá dos parámetros:
#  *      - Un array que sólo puede contener String con las palabras "run" o "jump"
#  *      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
#  * - La función imprimirá cómo ha finalizado la carrera:
#  *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
#  *        variará el símbolo de esa parte de la pista.
#  *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#  *      - Si hace "run" en "|" (valla), se variará la pista por "/".
#  * - La función retornará un Boolean que indique si ha superado la carrera.
#  * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
#  *

def validacion_pista(first,second):
    bucle = True
    while bucle:
        entrada = input(f"Pista:\n(Solamente puede contener \"{first}\" y/o \"{second}\"): ")
        for character in entrada:
            if character != first and character != second:
                break
            else:
                bucle = False
    return entrada

def validacion_corredor(first,second,third):
    entrada_total = list()
    bucle = True
    rellenado = 0
    while rellenado != third:
        entrada_parcial = (input(f"Corredor:\n(Han de introducirse {third} \
                                 acciones\)\n(Solamente puede contener \"{first}\" y/o \"{second}\"): "))
        if entrada_parcial == first or entrada_parcial == second:
            entrada_total.append(entrada_parcial)
            rellenado += 1
    return entrada_total

def competicion (pista,corredor,longitud_pista):
    superada = True
    pista = list(pista)
    for idx in range(0,longitud_pista):
        if pista[idx] == "|" and corredor[idx] == "run":
            pista[idx] = "/"
            superada = False
        elif pista[idx] == "_" and corredor[idx] == "jump":
            pista[idx] = "x"
            superada = False
    return pista, superada

pista = validacion_pista("_","|")

longitud_pista = len(pista)

corredor = validacion_corredor("run","jump",longitud_pista)

resultado = competicion(pista,corredor,longitud_pista)

print(f"El resultado de este corredor {corredor} en esta pista {pista} es {resultado}")