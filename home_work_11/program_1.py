def pair_sum(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                return True
    return False

num1 = [2, 4, 6, 8]
target1 = 10
result1 = pair_sum(num1, target1)
print(result1)

num2 = [1, 4, 5, 7]
target2 = 10
result2 = pair_sum(num2, target2)
print(result2)
