import random

nums = [random.randint(1, 100) for _ in range(15)]

print("Згенерований список:", nums)

v = sum(num for num in nums if num % 2 != 0)
a = sum(num for num in nums if num % 2 == 0)

if v > a:
    print("Так")
else:
    print("Ні")
