import random


rooms = [[[random.choice([True, False]) for r in range(20)] for f in range(15)] for t in range(3)]

vacancy = 0

for room_number in range(len(rooms[2][14][0:-1])):
    if rooms[2][14][room_number]:
        vacancy += 1

print(vacancy)
print(rooms[2][14])

i = 0
while i <= 3 :
    i += 2
    print("*")