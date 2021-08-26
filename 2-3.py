a = int(input('Введите целое число от 1 до 12: '))
vremena = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
if a in vremena[0]:
    print('wint')
elif a in vremena[1]:
    print('spring')
elif a in vremena[2]:
    print('summer')
elif a in vremena[3]:
    print('aut')
else:
    print('Числа от 1 до 12!')
