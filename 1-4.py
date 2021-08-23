vv = int(input('Здравствуйте, введите целое положительное число: '))
number = vv
max = 0
while number > 0:
    a = number % 10
    if a > max:
        max = a
        if max == 9:
            break
    number = number // 10
print(f"Самая большая цифра в числе {vv} - {max}")