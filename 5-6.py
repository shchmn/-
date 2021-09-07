summa = {}
with open("text_6.txt", encoding="utf-8") as new:
    for a in new:
        time = []
        less = ([b for b in a.split(" ")])
        for b in less:
            time.append(''.join(i for i in list(b) if i.isdigit()))
        summa[a.split(':')[0]] = sum([int(i) for i in time if i.isdigit()])
print(summa)
