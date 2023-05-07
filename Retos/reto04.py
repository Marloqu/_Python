# * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y
#   retornar el área de un polígono.
# * - La función recibirá por parámetro sólo UN polígono a la vez.
# * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# * - Imprime el cálculo del área de un polígono de cada tipo.


def area_tri_cuad_recta(tipo, base, altura = 1):
    if tipo == "Triángulo":
        return base * altura * 0.5
    elif tipo == "Cuadrado":
        return base * base
    elif tipo == "Rectángulo":
        return base * altura
    
print(area_tri_cuad_recta("Triángulo", 10, 5))

print(area_tri_cuad_recta("Cuadrado", 10, 5))

print(area_tri_cuad_recta("Rectángulo", 10, 5))
