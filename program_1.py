p = float(input("Введіть суму кредиту: "))
print("\nМісяць | Сума платежу | Процент")
print("-" * 40)

tp1 = 0

for m in range(1, 13):
    y1 = 1 if m <= 12 else 5
    mon = y1 * 12
    mir1 = 0.02 if y1 <= 2 else 0.04

    mp1 = p * mir1 / (1 - (1 + mir1) ** -mon)
    i1 = p * mir1
    p -= mp1 - i1
    tp1 += mp1

    print(f"{m:6} | {mp1:13.2f} | {i1:8.2f}")

print("\nМісяць | Сума платежу | Процент")
print("-" * 40)

tp2 = 0

for m in range(1, 61):
    y2 = 5
    mon = y2 * 12
    mir2 = 0.04

    mp2 = p * mir2 / (1 - (1 + mir2) ** -mon)
    i2 = p * mir2
    p -= mp2 - i2
    tp2 += mp2

    print(f"{m:6} | {mp2:13.2f} | {i2:8.2f}")
