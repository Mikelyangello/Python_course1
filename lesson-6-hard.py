# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.



class Toy:

    def __init__(self, name, color):
        self.name = name
        self.color = color


class ToyAnimal(Toy):

    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Животное'


class ToyMult(Toy):

    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Мультфильм'


class OtherToy(Toy):

    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Другая игрушка'


class ToyFactory:

    def create_toy(self, name, color, toy_type):
        self._buy_materials()
        self._making_form()
        self._print_color()
        if toy_type == 'Животное':
            print('Произведена игрушка-животное')
            return ToyAnimal(name, color)
        elif toy_type == 'Мультфильм':
            print('Произведена мульт-игрушка')
            return ToyMult(name, color)
        else:
            print('Получилось что-то непонятное..')
            return OtherToy(name, color)

    def _buy_materials(self):
        print('Закупка материалов.')

    def _making_form(self):
        print('Пошив игрушки.')

    def _print_color(self):
        print('Окраска игрушки.')


fabrika = ToyFactory()
toy = fabrika.create_toy('Винни-Пух', 'коричневый', 'Мультфильм')



# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка