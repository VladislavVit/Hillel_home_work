# Діапазон
v = list(range(10, 251))

# Фільтруємо
v = [e for e in v if e % 20 != 0]

# Виводимо результат
print(v)
