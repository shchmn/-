with open("text1.txt", "w", encoding='utf-8') as project:
    while True:
        a = input('Введите построчно текст, если закончили - пустую строку: ')
        if not a:
            break
        print(a, file=project)
