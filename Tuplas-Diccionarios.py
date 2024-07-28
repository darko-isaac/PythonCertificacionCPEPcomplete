school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break

    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score,2)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

print(sorted(school_class))

dic = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 4, 'f': 5, 'g': 6, 'h': 2, 'i': 7, 'j': 2, 'k': 8, 'l': 9}
dic2 ={'a': 1,'r': 4}
#esta linea de codigo hace uso del count en diccionarios para los valores contenidos en sus keys
duplicates = list(dic.values()).count(2)
print(duplicates)  # Output: 4
