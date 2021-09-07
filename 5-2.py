with open("text1.txt", "r", encoding='utf-8') as project:
    a = project.readlines()
    for num, num2 in enumerate(a, 1):
        words = len(num2.split())
        print(f'В {num} строке {words} слов(о)')
