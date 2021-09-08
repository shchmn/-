class Road:
    def __init__(self, l, w):
        self._lenght = l
        self._width = w

    def mass(self, ves=25, tols=5):
        return f"{self._lenght}м * {self._width}м * {ves}кг * {tols}см = " \
               f"{(self._lenght * self._width * ves * tols) / 1000} т"


r = Road(5000, 20)
print(r.mass())
