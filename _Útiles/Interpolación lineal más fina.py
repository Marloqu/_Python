# Función de interpolación lineal (obtener Y)

# Forma de llamar a esta función:

# variable_y_que_queremos_obtener_interpolada = round(interpolacion_lineal_y(datos, xdado),2)
# print(variable_y_que_queremos_obtener_interpolada)

def interpolacion_lineal_y(d, x):
    yinterpol = d[0][1] + ((d[1][1]-d[0][1]) / (d[1][0] - d[0][0]) * (x - d[0][0]))
    return yinterpol


datos = [[20, 40],[40, 80]]
xdado = 52
valor_y_interpolado = interpolacion_lineal_y(datos, xdado)

print(valor_y_interpolado)

# Función de interpolación lineal (obtener X)

# Forma de llamar a esta función:

# variable_x_que_queremos_obtener_interpolada = round(interpolacion_lineal_x(x0, y0, x1, y1, ydado),2)
# print(variable_x_que_queremos_obtener_interpolada)

def interpolacion_lineal_x(d, y):
    xinterpol = d[0][0] + ((d[1][0]-d[0][0]) / (d[1][1] - d[0][1]) * (y - d[0][1]))
    return xinterpol

datos = [[20, 40],[40, 80]]
ydado = 56
valor_x_interpolado = interpolacion_lineal_x(datos, ydado)

print(valor_x_interpolado)
