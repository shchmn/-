def fac(number):
    first = 1
    for n in range(number + 1):
        yield f'{n}! = {first}'
        first *= n +1

for numb in fac(int(input('Введите число: '))):
    print(numb)
