#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""


class Card:

    def __init__(self, name):
        import random
        self._name = name
        self._mycard = [i for i in random.sample(range(1, 91), 15)]
        self._list1 = sorted(self._mycard[0:5])
        self._list2 = sorted(self._mycard[5:10])
        self._list3 = sorted(self._mycard[10:15])
        for _ in range(4):
            self._list1.insert(random.randint(0, len(self._list1)), ' ')
            self._list2.insert(random.randint(0, len(self._list2)), ' ')
            self._list3.insert(random.randint(0, len(self._list3)), ' ')

    def check_numbers(self):
        counter = self._count_digits(self._list1) + self._count_digits(self._list2) + self._count_digits(self._list3)
        return counter

    def _count_digits(self, list):
        count_digits = 0
        for i in list:
            if str(i).isdigit():
                count_digits += 1
        return count_digits

    def get_name(self):
        return self._name

    def get_number(self, number):
        count_bochonok = self._mycard.count(number)
        if count_bochonok == 0:
            return False
        else:
            return True

    def _try_del_number(self, list, number):
        try:
            list[list.index(number)] = '-'
        except ValueError:
            pass

    def _del_number(self, number):
        self._try_del_number(self._list1, number)
        self._try_del_number(self._list2, number)
        self._try_del_number(self._list3, number)
        return True

    def _get_line(self, list):
        line = ''
        line = ''.join([str(i).rjust(3, ' ') for i in list])
        return line

    def get_card(self):
        return '{}\n{}\n{}'.format(self._get_line(self._list1),
                                   self._get_line(self._list2),
                                   self._get_line(self._list3))


class Loto_Game:

    def __init__(self, user_card, computer_card, name='SuperLoto'):
        self._user_card = user_card
        self._computer_card = computer_card
        self._meshok_list = list(range(1, 91))
        self._name = name
        self._bochonok = ''
        self._rounds = 0
        self._answer = 0
        self._cicle = True

    def _victory(self, winner):
        print('\n\nПобедил игрок {}\nЕго карточка\n{}\nСыграно раундов: {}\n'
              .format(winner.get_name(),
                      winner.get_card(),
                      self._rounds))

    def _fail(self, failer):
        print('\n\nИгрок {} проиграл.\nЕго карточка\n{}\nСыграно раундов: {}\n'
              .format(failer.get_name(),
                      failer.get_card(),
                      self._rounds))

    def _bochonok_choice(self):
        import random
        self._bochonok = random.choice(self._meshok_list)
        self._meshok_list.remove(self._bochonok)
        self._rounds += 1

    def start(self):
        import os
        print('\n***************************************\n'
              '{}, добро пожаловать в игру {}.\n'
              '***************************************\n'.format(os.getlogin().title(), self._name))
        while self._cicle:
            self._bochonok_choice()
            self._question()
            self._check_answer()
            self._check_all_cards()
            if self._cicle:
                print('\n*************\nСледующий раунд\n*************\n')
        print('\n_______________________\nСпасибо за игру.')

    def _check_all_cards(self):
        if self._user_card.check_numbers() == 0:
            self._victory(self._user_card)
            self._cicle = False
        elif self._computer_card.check_numbers() == 0:
            self._victory(self._computer_card)
            self._cicle = False

    def _question(self):
        self._answer = input('Новый бочонок: {} (осталось {})\n'
                         '---------------------------\n'
                         '------ Ваша карточка ------\n{}\n'
                         '---------------------------\n'
                         '--- Карточка компьютера ---\n{}\n'
                         '---------------------------\n'
                         'Зачеркнуть цифру y/n?: '.format(self._bochonok,
                                                          len(self._meshok_list),
                                                          self._user_card.get_card(),
                                                          self._computer_card.get_card()))

    def _check_card(self):
        if self._user_card.get_number(self._bochonok) and self._answer == 'y':
            return self._user_card._del_number(self._bochonok)
        elif self._user_card.get_number(self._bochonok) != (self._answer == 'n'):
            self._cicle = True
        else:
            self._fail(self._user_card)
            self._cicle = False

    def _computer_card_check(self):
        if self._computer_card.get_number(self._bochonok):
            return self._computer_card._del_number(self._bochonok)

    def _check_answer(self):
        while self._answer != 'y' and self._answer != 'n':
            self._answer = input('\n!!!!!!!!!!!!!!!\nОшибка при вводе.\n(для выхода из игры введите 0)\n'
                                 'Зачеркнуть цифру y/n?: ')
            if self._answer == '0':
                self._cicle = False
                break
        else:
            self._computer_card_check()
            return self._check_card()


card1 = Card('Внимательнейший')
card2 = Card('Компуктер')

game = Loto_Game(card1, card2, 'ЛОТИЩЕ!')
game.start()



