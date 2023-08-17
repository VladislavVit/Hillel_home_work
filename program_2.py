n = int(input("Введіть кількість рядків: "))

for i in range(n):
    print(str(i + 1).rjust(2, ' '),str("1" + i *"0").rjust(n, ' '))
