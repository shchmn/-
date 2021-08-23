one_hour = 3600
one_min = 60
print('Здравствуй! Я помогу перевести тебе секунды в часы и минуты')
sec = int(input('Введи секунды: '))
hour = sec // one_hour
minute = (sec - one_hour * hour) // one_min
second = sec - one_hour * hour - one_min * minute
print(f"{hour:02}:{minute:02}:{second:02}")
