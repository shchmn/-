rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("rus.txt", "w", encoding='utf-8') as project:
    with open("text_4.txt", "r", encoding='utf-8') as orig:
        project.writelines([a.replace(a.split()[0], rus.get(a.split()[0])) for a in orig])
