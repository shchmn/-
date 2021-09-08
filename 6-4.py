from random import choice


class Car:
    direc = ['направо', 'налево']

    def __init__(self, s, c, n, pol=False):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = pol

    def run(self):
        print(f'{self.name}: Машина поехала')

    def stop(self):
        print(f'{self.name}: Машина остановилась')

    def turn(self):
        print(f'{self.name}: Машина повернула {choice(self.direc)}')

    def show_speed(self):
        return f'Скорость машины {self.name}: {self.speed}'


class TownCar(Car):
    """Городская машина"""

    def show_speed(self):
        return f'Машина {self.name}, цвет: {self.color}, ' \
               f'превысила скорость! ({self.speed}км/ч)' if self.speed > 60 else f'Скорость машины {self.name}: ' \
                                                                             f'{self.speed} '


class SportCar(Car):
    """"Спортивная машина"""


class WorkCar(Car):
    """Рабочая машина"""

    def show_speed(self):
        return f'Машина {self.name}, цвет: {self.color}, ' \
               f'превысила скорость! ({self.speed}км/ч)' if self.speed > 40 else f'Скорость машины {self.name}: ' \
                                                                             f'{self.speed} '


class PoliceCar(Car):
    """Полицейская машина"""

    def __init__(self, s, c, n, pol=True):
        super().__init__(s, c, n, pol)


tc = TownCar(100, 'Черная', 'Городская')
sc = SportCar(100, 'Красная', 'Спортивная')
wc = WorkCar(10, 'Желтая', 'Рабочая')
pc = PoliceCar(90, 'голубая', 'Полицейская')

cars = [tc, sc, wc, pc]

for d in cars:
    d.run()
    print(d.show_speed())
    d.turn()
    d.stop()
    print()
