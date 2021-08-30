a = int(input('Введите первое число: '))
b = int(input('А теперь второе число: '))
if b == 0:
    print('На ноль не делим!')
else:
    def result(a, b):
        return a / b
    print(result(a, b))





a = int(input('Введите первое число: '))
b = int(input('А теперь второе число: '))


def result(a, b):
    while b == 0:
        try:
            result = a / 0
        except ZeroDivisionError:
            return "На ноль не делим!"
    else:
        result = a / b
        return round(result, 2)


print(result(a, b))