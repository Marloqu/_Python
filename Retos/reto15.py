# /*
#  * Reto #15
#  * ¿CUÁNTOS DÍAS?
#  * Fecha publicación enunciado: 11/04/22
#  * Fecha publicación resolución: 18/04/22
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
#  * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
#  * - La función recibirá dos String y retornará un Int.
#  * - La diferencia en días será absoluta (no importa el orden de las fechas).
#  * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.

import re

from datetime import date

def entrada_fecha(ordinal):
    pattern = r"[0-3][0-9]/[0-1][0-9]/[0-9][0-9][0-9][0-9]"
    while True:
        fecha = input(f"{ordinal} fecha: ")    
        if re.match(pattern,fecha) != None:
            fecha_validada = date(day=int(fecha[0:2]),month=int(fecha[3:5]),year=int(fecha[7:]))
            break
        else:
            print("El formato de la fecha a introducir es \"dd/MM/yyyy\"")
    return fecha_validada

def compara_fechas (fecha1, fecha2):
    diferencia = fecha1 - fecha2
    dias = abs(diferencia.days)
    return dias

fecha1 = entrada_fecha("Primera")

fecha2 = entrada_fecha("Segunda")

dias = compara_fechas(fecha1, fecha2)

print(f"La diferencia en días entre {fecha1} y {fecha2} es {dias}")

