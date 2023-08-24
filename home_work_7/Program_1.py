v = list(range(10, 251))

for i in v:
    if i % 20 == 0:
        v.remove(i)
print(v)
