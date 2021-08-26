some_list = list(input('Введите элементы списка: '))
for i in range(1, len(some_list), 2):
    some_list[i - 1], some_list[i] = some_list[i], some_list[i - 1]
print(some_list)
