
def function():

    for i in range(4):
        while True:

         try:

            temperature = float(input('Ingresa la temperatura actual:'))
            if temperature > 0:
                print("Por encima de cero")
                break
            elif temperature < 0:
                print("Por debajo de cero")
                break
            else:
                print("Cero")
                break

         except (ValueError, ArithmeticError,TypeError):
            print("Error: Entrada no válida. Por favor, ingresa un número natural." , e)


print(function())