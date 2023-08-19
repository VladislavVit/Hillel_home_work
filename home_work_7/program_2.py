rech = input("Введіть речення у якому більше 2-х слів: ")

# Розділ речення на список рядків
list = rech.split(" ")

# Видалення пустих рядків
list = [sl for sl in list if sl != ""]

# Перевірка відповідності вимогам
if len(list) <= 2:
    print("Введене речення має містити більше 2-х слів.")
else:
    # Сортування рядків
    list.sort()

    # Вивід даних в 2 колонки
    for index, sl in enumerate(list):
        print(f"{index + 1}\t{sl}")

    # Кількість слів
    print(f"Кількість слів: {len(list)}")

