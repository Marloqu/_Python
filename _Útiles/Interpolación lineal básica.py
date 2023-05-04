# Función de interpolación lineal (obtener Y)

# Forma de llamar a esta función:

# variable_y_que_queremos_obtener_interpolada = round(interpolacion_lineal_y(x0, y0, x1, y1, xdado),2)
# print(variable_y_que_queremos_obtener_interpolada)

def interpolacion_lineal_y(x0, y0, x1, y1, xdado):
    yinterpol = y0 + ((y1-y0) / (x1 - x0) * (xdado - x0))
    return yinterpol



valor_y_interpolado = interpolacion_lineal_y(-20, 0, -60, 60, 0)
print(valor_y_interpolado)

# Función de interpolación lineal (obtener X)

# Forma de llamar a esta función:

# variable_x_que_queremos_obtener_interpolada = round(interpolacion_lineal_x(x0, y0, x1, y1, ydado),2)
# print(variable_x_que_queremos_obtener_interpolada)

def interpolacion_lineal_x(x0, y0, x1, y1, ydado):
    xinterpol = x0 + ((x1-x0) / (y1 - y0) * (ydado - y0))
    return xinterpol


valor_x_interpolado = interpolacion_lineal_x(-20, 0, -60, 60, 0)
print(valor_x_interpolado)
