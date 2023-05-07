
# palabra1 = list(input())
# palabra2 = list(input())

def anagrama():
    palabra1 = input("Introduce primera palabra: ")
    palabra2 = input("Introduce segunda palabra: ")
    for item in palabra1:
        if (palabra2.count(item) == palabra1.count(item)) and palabra1 != palabra2:
            return True
        else:
            return False
print(anagrama())



