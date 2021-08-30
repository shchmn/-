x = float(input('Введите первое чиcло: '))
y = int(input('Введите второе чиcло: '))
if x < 0 or y > 0:
    print('x должен быть действительным положительным числом, а y целым отрицательным!')
else:
    def my_func(x, y):
        result = x ** y
        return result


    print(my_func(x, y))
