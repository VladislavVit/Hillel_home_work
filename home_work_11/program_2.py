function = lambda x, y=2: x ** y

num_list = [2, 3, 4, 5]
result1 = list(map(function, num_list))
print(result1)

num_list1 = [2, 3, 4]
num_list2 = [1, 2, 3]
result2 = list(map(function, num_list1, num_list2))
print(result2)
