multitres = "fizz"
multicinco = "buzz"
multiquince = multitres + multicinco

rango = range (1, 101)

for item in rango:
    if (item % 3) == 0:
        if (item % 5) == 0:
            item = multiquince
        item = multitres
    elif (item % 5) == 0:
        item = multicinco   
    print(item)

    