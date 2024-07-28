d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):

    d3.update(item)

print(d3)

colors = (("green", "#008000"), ("blue", "#0000FF"))
newDic = dict(colors)

print(newDic)

colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
}

for col, rgb in colors.items():
    print(col, ":", rgb)
    
