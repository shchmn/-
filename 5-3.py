with open ("text_3.txt", "r", encoding='utf-8') as project:
    work = {a.split()[0]: float(a.split()[1]) for a in project}
    print(f'Средняя зарплата = {round(sum(work.values()) / len(work), 3)}\n'
          f'А зарплату менее 20тыс получают: {[miz[0] for miz in work.items() if miz[1] < 20000]}')
