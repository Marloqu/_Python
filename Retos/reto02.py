fibonacci = [0, 1]

for item in range(2,50):
    fibonacci.append(item)
    fibonacci[item] = fibonacci[item - 1] + fibonacci[item - 2]

print(fibonacci)
