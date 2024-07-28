

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

email = "john.smith@pythoninstitute.org"

    # Encontrar el índice del carácter '@'
at_index = email.find('@')

    # Iterar a través de la cadena hasta el carácter '@'
for ch in email[:at_index]:
    print(ch, end="")

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue





