v = input("Введіть список чисел через пробіл: ")
c = [int(n) for n in v.split()]
elem = []

for num in c:
    if c.count(num) == 1 and num not in elem:
        elem.append(num)

result = ' '.join(map(str, elem))
print(result)
