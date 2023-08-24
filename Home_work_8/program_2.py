import random

v = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

N_input = input("Введіть розмір матриці у вигляді додатнього цілого числа: ")

if all(char in v for char in N_input) and int(N_input) > 0:
    N = int(N_input)
    matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(N)]

    for row in matrix:
        for num in row:
            print("{:<5}".format(num), end="")
        print()

    diagonal = sum(matrix[i][i] for i in range(N))
    print(f"Сума чисел по діагоналі: {diagonal}")

    column = sum(row[-1] for row in matrix)
    print(f"Сума чисел останнього стовбця: {column}")
else:
    print("Введені дані невірні. Потрібно ввести додатне ціле число.")
