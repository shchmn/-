a = input('Введите предложение: ')
for d, w in enumerate(a.split(), 1):
    if len(w) > 10:
        print(d, w[:10])
    else:
        print(d, w)
