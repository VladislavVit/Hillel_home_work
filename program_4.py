string = input("Введіть рядок (більше 15 символів): ")

if len(string) <= 15:
    print("Рядок має бути більше 15 символів.")
else:
    # a
    print("Третій символ:", string[2])

    # b
    print("Передостанній символ:", string[-2])

    # c
    print("Перші п'ять символів:", string[:5])

    # d
    print("Весь рядок, крім двох останніх символів:", string[:-2])

    # e
    print("Символи з парними індексами:", string[::2])

    # f
    print("Символи з непарними індексами:", string[1::2])

    # g
    print("Усі символи у зворотному порядку:", string[::-1])

    # h
    print("Символи через один у зворотному порядку:", string[-1::-2])

    # i
    print("Довжина рядка:", len(string))
