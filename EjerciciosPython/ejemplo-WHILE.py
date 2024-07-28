secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
secret_number = int(input("ingresa el nuemero"))
count = 0
while secret_number !=777:
    count += 1
    secret_number = int(input("ingresa el nuemero"))
print("adviniaste")

