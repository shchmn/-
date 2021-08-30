a = int(input('first'))
b = int(input('second'))
c = int(input('third'))


def my_func(a, b, c):
    return sum(sorted([a, b, c])[1:])


print(my_func(a, b, c))
