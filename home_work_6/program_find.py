string = input("Введіть рядок: ")
char = input("Введіть символ: ")
# Позиція символу
v = 0
# Знайдена позиція
f = []
# Пошук
while v < len(string):
    v = string.find(char, v)
    if v != -1:
        f.append(v)
        v += 1
    else:
        break

# Вивід результата пошуку
if f:
    for pos in f:
        print(f"Символ '{char}' знайдений на позиції: {pos}")
else:
    print(f"Символ '{char}' не знайдений у рядку.")
