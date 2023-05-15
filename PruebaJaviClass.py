
class Libro:
    def __init__(self, editorial, titulo, autor, paginas):
        self.editorial = editorial
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

print(type(Libro))

biblioteca = list()

print(type(biblioteca))

libro_1 = Libro("ESPASA", "El Quijote", "Miguel de Cervantes", 456)
libro_2 = Libro("SM", "Historia del comunismo", "Federico Jiménez Losantos", 233)
libro_3 = Libro("UPM", "Mecánica de medios continuos", "José María Fernández López", 689)

print(type(libro_1))

biblioteca = [libro_1, libro_2, libro_3]

print(type(biblioteca))

for idx in range(1,2):
    biblioteca.append(Libro(str(idx * "a"), str(idx * "b"), 2 * idx * "c" , idx * 10))
    

def printear(linea):
    print(biblioteca[linea].editorial)
    print(biblioteca[linea].titulo)
    print(biblioteca[linea].autor)
    print(biblioteca[linea].paginas)

for idx in range(0,len(biblioteca)):
    printear(idx)

print(type(biblioteca[1].editorial))
print(type(biblioteca[1]))





# biblioteca = [libro_1, libro_2]

# biblioteca.append(libro_3)

# print(biblioteca[2].editorial)
# 
# print(type(biblioteca))
# 
# print(libro_1.editorial)
# print(libro_2.titulo)
# print(libro_3.autor)
# print(libro_1.paginas)
# 
# print(type(Libro))
# 
# abcde = 14
# 
# print(type(abcde))
# 
# # print(type(Libro.editorial))
# # print(type(Libro.titulo))
# # print(type(Libro.autor))
# # print(type(Libro.paginas))
# 
# print(type(libro_1))
# print(type(libro_1.editorial))
# print(type(libro_1.titulo))
# print(type(libro_1.autor))
# print(type(libro_1.paginas))
