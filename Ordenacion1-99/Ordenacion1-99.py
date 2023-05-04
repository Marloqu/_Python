A1=input("Introduce un número cualquiera ")
A2=input("Introduce un número cualquiera ")
A3=input("Introduce un número cualquiera ")
print("Éstos son los números que has introducido:",A1,A2,A3)
print("La ordenación de mayor a menor de estos 3 números es la siguiente:")
A1f=float(A1)
A2f=float(A2)
A3f=float(A3)

if A1f>A2f:
    if A2f>A3f:
        print(A1f,A2f,A3f)
    elif A1f>A3f:
        print(A1f,A2f,A3f)
elif A2f>A3f:
    if A1f>A3f:
        print(A2f,A1f,A3f)
    else:
        print(A2f,A3f,A1f)
else:
    print(A3f,A2f,A1f)
