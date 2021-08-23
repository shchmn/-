while True:
    days = 1
    start = float(input('Сколько километров пробежал в первый день: '))
    goal = float(input('Сколько нужно пробежать: '))

    while start < goal:
        start = start + start * 0.1
        days = days + 1
    print(f"Нужного результата спортсмен добьется к {days} дню")
    break
