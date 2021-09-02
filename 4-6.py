from itertools import count, cycle

some_count = count(7)
some_cycle = cycle('qwerty')

for n in range(10):
    print(next(some_cycle), next(some_count))
