# Función de validación de entrada numérica a través de un input

# Forma de llamar a esta función:

# variable_que_queremos_usar_ya_validada = entrada_numerica_y_validacion("Descrición del texto que queremos mostrar durante el input")
# print(variable_que_queremos_usar_ya_validada)

def entrada_numerica_y_validacion(descripcion_variable_a_validar):
    while True:
        try:
            variable_a_validar = float(input(f"{descripcion_variable_a_validar}: "))
            break
        except ValueError:
            print("No es un valor numérico correcto")
    variable_validada = abs(variable_a_validar)
    return variable_validada
