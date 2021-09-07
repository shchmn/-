from random import randint
with open("rand.txt", "w", encoding="utf-8") as new:
    some_l = [randint(1, 20) for a in range(20)]
    new.write(" ".join(map(str, some_l)))
print(f"Сумма - {sum(some_l)}")
