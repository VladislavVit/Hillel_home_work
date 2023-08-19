string = input("Введіть рядок: ")
char = input("Введіть символ: ")

v = 0

found_positions = []

while v < len(string):
    v = string.find(char, v)
    if v != -1:
        found_positions.append(v)
        v += 1
    else:
        break


if found_positions:
    for pos in found_positions:
        print(f"Символ '{char}' знайдений на позиції: {pos}")
else:
    print(f"Символ '{char}' не знайдений у рядку.")
