v = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

N = input("Введіть розмір матриці у вигляді додатнього цілого числа: ")

if all(i in v for i in N) and int(N) > 0:
    N = int(N)
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            if i % 2 == 0:
                row.append(j - N)
            else:
                row.append(i + 1)
        matrix.append(row)

    for row in matrix:
        for num in row:
            print("{:<4}".format(num), end="")
        print()
else:
    print("Введені дані невірні. Потрібно ввести додатне ціле число.")
