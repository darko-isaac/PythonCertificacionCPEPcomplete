altura = int(input("Por favor, ingrese la altura del pino: "))

# Dibujar el pino
for i in range(altura):
    # Dibujar cada fila del pino
    for j in range(i + 1):
        # Calcular el número de espacios y asteriscos
        espacios = altura - j - 1
        asteriscos = 2 * j + 1
        # Imprimir los espacios y asteriscos
        print(' ' * espacios + '*' * asteriscos)

# Dibujar el tronco del pino
tronco_anchura = 3
tronco_altura = 2
espacios_tronco = altura - 1
for i in range(tronco_altura):
    print(' ' * (espacios_tronco - 1) + '*' * tronco_anchura)