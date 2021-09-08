class Stationery:
    def __init__(self, title='выбранным предметом'):
        self.title = title


    def draw(self):
        print(f'Рисуй {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} ручка для рисования')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} карандаш для рисования')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} маркер для рисования')

st = Stationery()
pen = Pen('Красная')
penc = Pencil('Зеленый')
han = Handle('Розовый')

sl = [st, pen, penc, han]

for d in sl:
    d.draw()
