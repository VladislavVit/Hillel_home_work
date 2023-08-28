import random

dict_1 = {f'key_{i}': random.randint(1, 10) for i in range(1, 21)}

print("Початковий словник:")
print(dict_1)

v = 1
for value in dict_1.values():
    v *= value

print("\nРезультат множення чисел:", v)
