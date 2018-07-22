# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import easy


def Programm():
    print('\n\n**********************************************************\n\n'
          'Добро пожаловать в консольную программу работы с каталогами!\n')
    action_arg = True
    while action_arg:
        user_choice = easy.main_menu()
        action_arg = easy.check_input(user_choice)
    print('\nСпасибо. Всего доброго!'
          '\n\n**********************************************************\n\n')


Programm()
