def summa():
    a = 0
    while True:
        list_n = input('Введите числа, которые хотели бы сложить (для выхода из программы нажмите q: ').split()
        for number in list_n:
            if number == "q" or number == "Q":
                return a
            else:
                try:
                    a += int(number)
                except ValueError:
                    print('Для выхода из программы нажмите q: ')
        print(f"Сумма введенных чисел = {a}")


print(summa())
