v1 = [2, 5, 2, 4, 3, 5, 9, 7]
v2 = [3, 8, 0, 6, 7, 9]

count = len(set(v1) & set(v2))

print("Кількість різних чисел в обох списках:", count)