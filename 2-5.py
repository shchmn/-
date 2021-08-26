score = [9, 8, 7, 6, 5, 5, 4, 3]
a = int(input('введи цифру: '))
if a <= score[-1]:
    score.append(a)
for i in score:
    if i < a:
        score.insert(score.index(i), a)
        break
print(score)
