# CÁLCULO MOMENTO ÚLTIMO DE VIGAS DE HORMIGÓN ARMADO

tipo_armadura = { # Creación del diccionario de materiales posibles; fyk en MPa
    "B400": 400,
    "b400": 400,
    "B500": 500,
    "b500": 500,
    "B600": 600,
    "b600": 600
}

# Solicitud del tipo de armadura y validación de que la entrada es correcta

tipo_armadura_input = ""
while not tipo_armadura_input in tipo_armadura.keys():
    tipo_armadura_input = input("¿Tipo de armadura (B400, B500 ó B600)? ")
fyk = tipo_armadura[tipo_armadura_input] # Lee el fyk desde el diccionario de materiales

# Solicitud de datos necesarios para calcular

area_armadura_input = ""
while type(area_armadura_input) != float and type(area_armadura_input) != int:
    area_armadura_input = input("Sección de armadura en cara inferior (cm2): ")
seccion_As = area_armadura_input

#canto_h_input = ""
while not float(canto_h_input):
    canto_h_input = float(input("Sección de armadura en cara inferior (cm2): "))
canto_h = canto_h_input

# MRd Definición de función para calcular momento resistente último

def calculo_momento_resistente(value_seccion_armadura,value_canto_h,value_fyk=500):
    return_MRd = 0.9 * value_seccion_armadura * (0.9 * value_canto_h) * fyk/1000/1.15
    return(return_MRd)

# MRd Cálculo_momento_resistente(sección_armadura,canto_pieza_h,fyk)

MRd = calculo_momento_resistente(sección_armadura,canto_pieza_h)


print(sección_armadura, canto_pieza_h, fyk)

print(MRd)



