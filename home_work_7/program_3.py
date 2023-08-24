list1 = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
list2 = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23, 934]

l1_in_l2 = [list2.count(num) for num in list1]
l2_in_l1 = [list1.count(num) for num in list2]

print("{:<10} {:<10}".format("Число", "Кількість"))

for i in range(len(list1)):
    print("{:<10} {:<10}".format(list1[i], l1_in_l2[i]))

print("\n{:<10} {:<10}".format("Число", "Кількість"))

for i in range(len(list2)):
    print("{:<10} {:<10}".format(list2[i], l2_in_l1[i]))
