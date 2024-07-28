'''
bloques = int(input("Por favor, ingrese el número de bloques: "))

altura = 0
bloques_usados = 0

# Iterar a través de un rango desde 1 hasta el número total de bloques más 1
for i in range(1, bloques):
    # Calcular los bloques necesarios para la nueva altura
    bloques_usados += i
    # Si no hay suficientes bloques para la siguiente capa, se rompe el bucle
    if bloques_usados > bloques:
        break
    # Incrementar la altura para la siguiente capa
    altura += 1

print("La altura de la pirámide es", altura)

'''

collats = int(input("Por favor, ingrese colatz: "))
numPaso = 0

while collats != 1:

    if collats % 2 == 0:
        collats = collats // 2

    else:
        collats = 3 * collats + 1
    print(collats)
    numPaso += 1



print("Pasos:", numPaso)




