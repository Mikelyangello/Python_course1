# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:

    def __init__(self, name='default_player', health=100, damage=10, armor=1, exp=0, lvl=1):
        self._name = name
        self._health = health
        self._damage = damage
        self._armor = armor
        self._exp = exp
        self._lvl = lvl

    def _attack_damage(self, enemy_armor):
        return round(self._damage / enemy_armor, 1)

    def _victory(self, enemy):
        enemy._set_health(0)
        print('Victory! The enemy {} is dead.\n{} win with {} health!.'.format(enemy.get_name(), self.get_name(), self.get_health()))

    def get_armor(self):
        return self._armor

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def _set_health(self, count):
        self._health = count

    def attack(self, enemy):
        print('Атакует: {}\nОбороняется: {}'.format(self.get_name(), enemy.get_name()))
        enemy_armor = enemy.get_armor()
        total_damage = self._attack_damage(enemy_armor)
        result = enemy.get_health() - total_damage
        if result <= 0:
            return self._victory(enemy)
        else:
            print('Нанесен урон {}dmg игроку {}. Остаток его здоровья: {}'
                  '\n------------\n'.format(total_damage, enemy.get_name(), result))
            return enemy._set_health(result)


class Player(Person):

    def __init__(self, name='default_player', health=100, damage=10, armor=1, exp=0, lvl=1):
        super().__init__(name, health, damage, armor, exp, lvl)
        self._health = health + 30
        self._damage = damage + 5
        self._armor = armor * 0.9


class Enemy(Person):

    def __init__(self, name='default_player', health=100, damage=10, armor=1, exp=0, lvl=1):
        super().__init__(name, health, damage, armor, exp, lvl)
        self._health = health - 50
        self._damage = damage + 15
        self._armor = armor * 1.5


class The_Game:

    def __init__(self, player1, player2, name='The buttle'):
        self._player1 = player1
        self._player2 = player2
        self._name = name
        print('\n------------------\n'
              'Начинается {} между игроками: \n{}    и    {}'.format(self._name,
                                                                     self._player1.get_name(),
                                                                     self._player2.get_name()))

    def random_attack(self):
        import random
        var = random.randrange(1, 3)
        if var == 1:
            return self._player1.attack(self._player2)
        else:
            return self._player2.attack(self._player1)

    def start(self):
        while self._player1.get_health() > 0 and self._player2.get_health() > 0:
            result = self.random_attack()
        return print('Спасибо за игру. {} завершился.'.format(self._name))


player1 = Player('Pl1')
player2 = Enemy('Pl2')
game = The_Game(player1, player2, 'Партейка')

game.start()

