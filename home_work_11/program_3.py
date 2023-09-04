import random


def prime_nums(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generator(n, z):
    for num in range(n, z + 1):
        if prime_nums(num):
            yield num


N = random.randint(1, 50)
Z = random.randint(51, 100)

print(f"Числа в діапазоні від {N} до {Z}:")
numbers = list(generator(N, Z))
print(" ".join(map(str, numbers)))
