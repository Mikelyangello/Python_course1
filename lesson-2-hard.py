# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

new_list = equation.split(' ')
for i in new_list:
    while i.count('x') == 0:
        break
    else:
        k = float(i[:i.index('x')])

y = k * x + float(new_list[-1])
print(equation, '\nx =', x, '\ny =', y)

print('\n_________________________________________\n')

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)


while True:
    user_date = input('Введите дату в формате dd.mm.yyyy:\n').split('.')
    dlina_elementov_daty = []
    user_data_int_list = []
    true_counter = 0

    for i in user_date:
        if i.isdigit():
            dlina_elementov_daty.append(len(i))
            user_data_int_list.append(int(i))

    if len(user_date) == 3 and dlina_elementov_daty == [2, 2, 4]:

        if user_data_int_list[1] in [1, 5, 7, 8, 10, 12]:
            for j in user_data_int_list:
                if 1 <= j <= [31, 12, 9999][user_data_int_list.index(j)]:
                    true_counter += 1

        elif user_data_int_list[1] == 2 and user_data_int_list[2] % 4 == 0:
            for j in user_data_int_list:
                if 1 <= j <= [29, 12, 9999][user_data_int_list.index(j)]:
                    true_counter += 1

        elif user_data_int_list[1] == 2:
            for j in user_data_int_list:
                if 1 <= j <= [28, 12, 9999][user_data_int_list.index(j)]:
                    true_counter += 1

        else:
            for j in user_data_int_list:
                if 1 <= j <= [30, 12, 9999][user_data_int_list.index(j)]:
                    true_counter += 1

        if true_counter == 3:
            print('Наконец-то верный ввод. Спасибо!')
            break

    print('Неверный ввод. Повторите попытку.')

print('\n_________________________________________\n')

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

user_room = int(input('Введите номер интересующей Вас комнаты (диапазон 1 - 2 000 000 000):\n'))
block_number = 0
stages_of_building = 0
rooms_counter = 0

while True:
    block_number += 1
    stages_of_building += block_number
    rooms_counter += block_number ** 2
    if rooms_counter >= user_room:
        break

delta = rooms_counter - user_room
stage = stages_of_building - delta // block_number
room_on_the_stage = block_number - (delta - (stages_of_building - stage) * block_number)

print('Ваша комната №{} находится на {} этаже, {} слева'.format(user_room, stage, room_on_the_stage))