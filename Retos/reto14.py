#  * Reto #14
#  * ¿ES UN NÚMERO DE ARMSTRONG?
#  * Fecha publicación enunciado: 04/04/22
#  * Fecha publicación resolución: 11/04/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
#  * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.

def verifica_armstrong(num):
    desglosado = list(str(num))
    n_esima = len(desglosado)
    compuesto = 0
    for idx in range (0, n_esima):
        compuesto += int(desglosado[idx])**n_esima
    return compuesto == num        

numero = int(input("¿Cuál número hay que verificar: "))

print(f"¿El número {numero} es de Armstrong?: {verifica_armstrong(numero)}")


