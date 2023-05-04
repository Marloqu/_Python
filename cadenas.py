multiline = """Facts about the Moon:
  There is no atmosphere.
  There is no sound."""
print(multiline)

print("temperatures and facts about the moon".title())

heading = "temperatures and facts about the moon"
print(heading.title())

temperatures = """Daylight: 260 F
Nighttime: -280 F"""
print(temperatures.split('\n'))


temperatures.split('\n')

print("----------------------------------------")

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
while Mars has -28 Celsius."""
resultadolower=temperatures.lower()
resultado=resultadolower.find("e")
print(resultado)
resultado=resultadolower.count("e")

print(resultado)



print("----------------------------------------------------------------------------------")

nveces = input("¿Cuántos números quieres listar?")
nveces=int(nveces)

print(f"Los números del 1 al {nveces} son los siguientes:")
n=1
while n <= nveces:
    print(f"El número {n**3}")
    n=n+1


lista=list([1,2,3,4,5,6,7,8,9,10])
print(lista[-1])
lista.reverse()
print(lista[-1])





