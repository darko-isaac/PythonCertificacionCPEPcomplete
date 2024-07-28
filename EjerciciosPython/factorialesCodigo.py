def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(-1, 6):  # probando
    print(n, factorial_function(n))

listanew = [[i + 2 for i in range(5)] for j in range(20)]

# Imprimir la lista resultante
for sublist in listanew:
    print(sublist)