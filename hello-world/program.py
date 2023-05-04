# program.py
sum = 1 + 2 # 3
product = sum * 2
print(sum)
print(sum*2+500.522)
product2=sum*2+99999.2222
print(product)
print(product2)
print("-----------------------------")
result1=type(sum)
print(result1)
print("-----------------------------")
RESULT2=type(product)
print(RESULT2)
result3=type(product2)
print(result3)
product +=2
print(product)
product=product*5
print(product)
cadena="kaka de la vaca"
cadena2="1       "+cadena+"                "+cadena
print(cadena,cadena2)
from datetime import date
print(date.today())
fecha=date.today()

print("hoy es un día cojonudo"+str(fecha))
print("    ")

factorconversion=3.26 # 1 3,26 añoluz/parsec

parsecs_input=input("¿Cuantos parsecs quiere convertir en años luz?")

lightyears=float(parsecs_input)*factorconversion
print(str(parsecs_input)+" parsecs is "+str(lightyears)+" lightyears")

print("-----------------------------")

lightyears2=float(parsecs_input)*factorconversion
print(str(parsecs_input)+" parsecs is "+str(lightyears2)+" lightyears")



      

