num = int(input("Загадайте число від 0 до 100: "))

count = 0
# Діапазон
low = 0
high = 100
# Чесність
true = True

while True:
    # Середне значення
    g = (low + high) // 2
    count += 1
    # Отримання числа та перебор
    v = input(f"Чи це число {g}? Введіть 'більше', 'менше' або 'так': ")

    if v == 'так':
        if g == num:
            print(f"Вгадане число: {num}")
            print(f"Кількість кроків: {count}")
        else:
            print("Користувач не чесний.")
        break
    elif v == 'більше':
        low = g + 1
    elif v == 'менше':
        high = g - 1
    else:
        print("Будь ласка, введіть 'більше', 'менше' або 'так'.")
    # Перевірка на чесність.
    if (v == 'більше' and g >= num) or (v == 'менше' and g <= num):
        true = False
        break

if not true:
    print("Користувач не чесний.")
