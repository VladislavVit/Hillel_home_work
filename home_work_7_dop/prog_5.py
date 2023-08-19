n = int(input("Введіть n: "))
m = int(input("Введіть m: "))

a = []

for i in range(n):
    v = []
    for j in range(m):
        if (i + j) % 2 == 0:
            v.append(".")
        else:
            v.append("*")
    a.append(v)

for v in a:
    print(' '.join(v))
