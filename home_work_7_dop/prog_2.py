v = input("Введіть список чисел через пробіл: ")
c = [int(n) for n in v.split()]
p = sum(1 for n in c if n > 0)
print(f"Кількість додатних елементів: {p}")
