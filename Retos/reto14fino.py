
def verifica_armstrong(num):
    desglosado = list(str(num))
    n_esima = len(desglosado)
    compuesto = 0
    for item in desglosado:
        compuesto += int(item)**n_esima
    return compuesto == num        

numero = int(input("¿Cuál número hay que verificar: "))

print(f"¿El número {numero} es de Armstrong?: {verifica_armstrong(numero)}")