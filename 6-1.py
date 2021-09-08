from time import sleep


class TrafficLight:
    __color = 'Черный'

    def running(self):
        while True:
            print('Красный')
            sleep(7)
            print('Жёлтый')
            sleep(2)
            print('Зеленый')
            sleep(5)
            print('Жёлтый')
            sleep(2)


tl = TrafficLight()
tl.running()
