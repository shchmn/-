from sys import argv

script, name, hour, one_hour, prime = argv

print('Имя скрипта: ', script)
print('ФИО работника: ', name)
print('Количество часов: ', hour)
print('Стоимость 1 часа: ', one_hour)
print('Премия: ', prime)

print(f"Зарплата = {(float(hour) * float(one_hour) + float(prime))}")
