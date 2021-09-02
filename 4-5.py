from functools import reduce
some_list = list(range(99, 1001))
new_list = [n for n in some_list if n % 2 == 0]


def proi(a, b):
    return a * b


result = reduce(proi, new_list)
print(result)

"-----------------------------------------------------------------------"

from functools import reduce
some_list = list(range(99, 1001))
new_list = [n for n in some_list if n % 2 == 0]
print(new_list)
proi = reduce(lambda a, b: a * b, new_list)
print(proi)
