v = input("Введіть послідовність цілих чисел через пробіл: ")
c = [int(num) for num in v.split()]
f = c[-2:]
c = c[:-2]
c = f + c
print(c)
