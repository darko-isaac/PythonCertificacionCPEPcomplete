import random

temps = [[random.uniform(30, 1) for h in range(24)] for d in range(31)]

total = 0

for day in temps:
    total += day[11]

average = total / 31

print("Temperatura promedio al mediodía:", average)
print(temps)

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("La temperatura más alta fue:", highest)
for day in temps[:18]:
    for temp in day:
        if temp > highest:
            highest = temp

print("La temperatura más alta del 14:", max(temps[13][:12]))
