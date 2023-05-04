# CÁLCULO MOMENTO ÚLTIMO DE VIGAS DE HORMIGÓN ARMADO

# Creación del diccionario de materiales posibles; fyk en MPa

tipo_armadura = { 
    "B400": 400,
    "b400": 400,
    "B500": 500,
    "b500": 500,
    "B600": 600,
    "b600": 600
}

# Función de validación de entrada numérica a través de un input

def entrada_numerica_y_validacion(descripcion_variable_a_validar):
    while True:
        try:
            variable_a_validar = float(input(f"{descripcion_variable_a_validar}: "))
            break
        except ValueError:
            print("No es un valor numérico correcto")
    variable_validada = abs(variable_a_validar)
    return variable_validada

# MRd Definición de función para calcular momento resistente último

def calculo_momento_resistente(value_seccion_As,value_canto_h,fyk):
    return_MRd = 0.9 * value_seccion_As * (0.9 * value_canto_h) * (fyk / 1.15) / 1000
    return(return_MRd)

# Solicitud del tipo de armadura y validación de que la entrada es correcta

tipo_armadura_input = ""
while not tipo_armadura_input in tipo_armadura.keys():
    tipo_armadura_input = input("¿Tipo de armadura (B400, B500 ó B600)? ")
fyk = tipo_armadura[tipo_armadura_input] # Lee el fyk desde el diccionario de materiales

# Solicitud de área de armadura, incluso validación de entrada correcta

seccion_As = entrada_numerica_y_validacion("Sección de armadura en cara inferior (cm2)")

# Solicitud de área de armadura, incluso validación de entrada correcta

canto_h = entrada_numerica_y_validacion("Canto de la pieza (cm)")

# MRd Cálculo_momento_resistente(seccion_As,canto_h,fyk)

MRd = round(calculo_momento_resistente(seccion_As,canto_h,fyk),2)

# Salida final del resultado

print(f"Una viga con un canto de {round(canto_h)} cm con {round(seccion_As,2)} cm2 de armadura B{fyk} tiene un MRd aproximado de {MRd} kNm")
