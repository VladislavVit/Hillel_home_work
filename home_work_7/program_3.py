list1 = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
list2 = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23, 934]

count = {num: 0 for num in list1}

for num in list2:
    if num in count:
        count[num] += 1

print("{:<10} {:<10}".format("Число", "Кількість"))

for num, count in count.items():
    print("{:<10} {:<10}".format(num, count))
