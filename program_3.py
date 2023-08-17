n = input("Введіть число від 3 до 9: ")


n = int(n)
if 3 <= n <= 9:
    for i in range(1, n + 1):
        v = ''.join(str(j) for j in range(1, i + 1))
        m = v + v[-2::-1]
        print(m.ljust(n * 2 - 1))
else:
    print("Число повинно бути від 3 до 9.")

