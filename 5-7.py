from json import dump
with open('text_7.txt', 'r', encoding='utf-8') as f_file:
    with open('text_77.json', 'w', encoding='utf-8') as s_file:
        some_d = {a.split()[0]: int(a.split()[2]) - int(a.split()[3]) for a in f_file}
        firm = []
        for b in some_d.values():
            if b > 0:
                firm.append(b)
        dump([some_d, {"average_profit": sum(firm) / len(firm)}], s_file, ensure_ascii=False, indent=4)
