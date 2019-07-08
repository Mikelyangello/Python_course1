# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:

    def __init__(self, name, color, speed=60, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала'.format(self.name))

    def stop(self):
        print('Машина {} остановилась'.format(self.name))

    def turn(self, direction='прямо'):
        print('Машина {} повернула {}'.format(self.name, direction))


class SportCar:

    def __init__(self, name, color='red', speed=300, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала'.format(self.name))

    def stop(self):
        print('Машина {} остановилась'.format(self.name))

    def turn(self, direction='прямо'):
        print('Машина {} повернула {}'.format(self.name, direction))

class WorkCar:

    def __init__(self, name, color, speed=90, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала'.format(self.name))

    def stop(self):
        print('Машина {} остановилась'.format(self.name))

    def turn(self, direction='прямо'):
        print('Машина {} повернула {}'.format(self.name, direction))

class PoliceCar:

    def __init__(self, name, color='white', speed=250, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала'.format(self.name))

    def stop(self):
        print('Машина {} остановилась'.format(self.name))

    def turn(self, direction='прямо'):
        print('Машина {} повернула {}'.format(self.name, direction))


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:

    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала'.format(self.name))

    def stop(self):
        print('Машина {} остановилась'.format(self.name))

    def turn(self, direction='прямо'):
        print('Машина {} повернула {}'.format(self.name, direction))


class TownCar(Car):

    def __init__(self, name, color, speed=60, is_police=False):
        super().__init__(name, color, speed, is_police)


class SportCar(Car):

    def __init__(self, name, color='red', speed=300, is_police=False):
        super().__init__(name, color, speed, is_police)


class WorkCar(Car):

    def __init__(self, name, color, speed=90, is_police=False):
        super().__init__(name, color, speed, is_police)


class PoliceCar(Car):

    def __init__(self, name, color='white', speed=250, is_police=True):
        super().__init__(name, color, speed, is_police)


nypd = PoliceCar('POLICIA')
nypd.go()
nypd.turn('налево')
nypd.go()
nypd.stop()