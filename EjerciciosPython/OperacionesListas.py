my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temp_list = []

for item in my_list:
    duplicate_found = False
    for unique_item in temp_list:
        if item == unique_item:
            duplicate_found = True
            break
    if not duplicate_found:
        temp_list.append(item)

print("La lista con elementos únicos:")
print(temp_list)