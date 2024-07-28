my_list = [3, 7, 10, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

my_list.sort()
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] < my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

my_list.sort()
valormax = max(my_list)
print(valormax)

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13,65]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)