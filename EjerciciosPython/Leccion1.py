num1=0
mi_array = []

# Usamos un bucle for para llenar el array con los cuadrados de los números del 1 al 5
for i in range(0, 6):
    cuadrado = i ** 2
    mi_array.append(cuadrado)
    #si el print lo pongo dentro del for, imprime todo el array subsecuentemente
    print(mi_array)
#imprime todo lo que tiene el array pero debe haber un espacion para reconocer que es fuera
#del ciclo for, de lo contrario imprimiria solo el valor del ultimo ciclo
print(mi_array)
load = 9
load **= 0.5

print(load)
a = 3.0
b = 4.0
c = ((a ** 2 )+ (b ** 2)) ** 0.5
print("c =", c)
print(64 ** 0.5)

mi_array2 = [0,1,-1]
mi_array3=[]
for i2 in range(0,3):
    x = mi_array2[i2] # Codifica tus datos de prueba aquí.
    x = float(x)
    # Escribe tu código aquí.
    y=(3*x**3)-(2*x**2)+(3*x)-1

    mi_array3.append(y)
    print("y =", y)
print(mi_array3)

bool validar=True,False


expo=2 ** 2 ** 3
print(expo)
#3x3 - 2x2 + 3x - 1
div = 22//11
print(div)