some_list = [5, 5, 6, 3, 43, 56, 56, 78, 56, 4, 2, 1]
new_list = [n for n in some_list if some_list.count(n) < 2]
print(new_list)
