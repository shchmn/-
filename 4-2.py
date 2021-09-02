some_list = [4, 6, 2, 87, 4, 67]
new_list = [some_list[n] for n in range(1, len(some_list)) if some_list[n] > some_list[n - 1]]
print(new_list)
