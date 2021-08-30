def int_func():
    words = input('Введите слова, используя латинские буквы в нижнем регистре, через пробел: ').split()
    for a in words:
        sch = 0
        for i in a:
            if 97 <= ord(i) <= 122:
                sch += 1
        print(a.title() if sch == len(a) else f"{a} - ай, ты не выполнил условия!")


int_func()
