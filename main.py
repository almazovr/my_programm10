import math
while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Выход")

    choice = input("Введите номер операции: ")

    if choice == "11":
        break

    try:
         choice = int(choice)
    except ValueError:
        print("боже, что читать не умешь?! Выбери из того что предлогают")
        continue

    if choice < 1 or choice > 10:
        print("боже, что читать не умешь?! Выбери из того что предлогают")
        continue

    if choice in [1, 2, 3, 4, 5]:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Некорректный ввод чисел.")
            continue

    if choice == 1:
        result = num1 + num2
        print("ответ: ", result)
    elif choice == 2:
        result = num1 - num2
        print("ответ: ", result)
    elif choice == 3:
        result = num1 * num2
        print("ответ: ", result)
    elif choice == 4:
        if num2 == 0:
            print("ты что в школе не был и не знаешь что на 0 делить нельзя?")
        else:
            result = num1 / num2
            print("ответ: ", result)
    elif choice == 5:
        result = math.pow(num1, num2)
        print("ответ: ", result)
    elif choice == 6:
        if num1 < 0:
            print("как так?!: квадратный корень из отрицательного числа.")
        else:
            result = math.sqrt(num1)
            print("ответ: ", result)
    elif choice == 7:
        if num1 < 0:
            print("как так?!: факториал из отрицательного числа.")
        else:
            result = math.factorial(int(num1))
            print("ответ: ", result)
    elif choice == 8:
        result = math.sin(num1)
        print("ответ: ", result)
    elif choice == 9:
        result = math.cos(num1)
        print("ответ: ", result)
    elif choice == 10:
        result = math.tan(num1)
        print("ответ: ", result)