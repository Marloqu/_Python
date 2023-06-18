# * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión
# están equilibrados.
# * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# * - Expresión no balanceada: { a * ( c + d ) ] - 5 }

def comprobacion(expresion):
    expresion = str(expresion)
    caracteres_a_comprobar = ["(", "[", "{", ")", "]", "}"]
    limpio = []
    for element in expresion:
        if element in caracteres_a_comprobar:
            limpio.append(element)
        print(limpio)
    while len(limpio) != 0:
        for idx in range(0, len(limpio) - 1):
            if ((limpio[idx + 1] == ")" and limpio[idx] == "(") or
                (limpio[idx + 1] == "]" and limpio[idx] == "[") or
                (limpio[idx + 1] == "}" and limpio[idx] == "{")):
                limpio.pop(idx + 1)
                limpio.pop(idx)
                print(limpio)
                break
            
            
            # elif ((limpio[1] == ")" and limpio[0] == "(") or
            #     (limpio[1] == "]" and limpio[0] == "[") or
            #     (limpio[1] == "}" and limpio[0] == "{")):
            #     resultado = "SÍ"
            else:
                resultado = "NO"
    
    print(f"La expresión \"{expresion}\" {resultado} está balanceada")
    
expresion = input("Expresión a comprobar: ")

comprobacion(expresion)
