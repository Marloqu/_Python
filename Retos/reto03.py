def comprobar_primo(numero):
    for idx in range(1, numero):
        if numero % idx == 0 and idx != 1:
            return False
            break
        elif idx == numero -1:
            return True

numero_entrada = int(input("Introduce un número entero positivo para comprobar si es primo: "))

if comprobar_primo(numero_entrada):
    print(f"El número {numero_entrada} SÍ es primo")
else:
    print(f"El número {numero_entrada} NO es primo")

primos_a_listar = int(input("Introduce cuál es el límite superior de números primos que quieres listar: "))

for idx in range(1, primos_a_listar + 1):
    if comprobar_primo(idx):
        print(idx)
