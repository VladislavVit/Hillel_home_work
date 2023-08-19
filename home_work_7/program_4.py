v = input("Введіть список цілих чисел через пробіл: ")
c = [int(num) for num in v.split()]

max = c.index(max(c))
min = c.index(min(c))

c[max], c[min] = c[min], c[max]

result = ' '.join(map(str, c))
print(result)
