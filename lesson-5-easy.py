# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


import os
import sys
import shutil


def make_dirs(start=1, stop=10):
    # функция создания директорий в диапазоне dir_1-dir9 в папке, где запущен скрипт
    for i in range(start, stop):
        my_path = os.path.join(os.getcwd(), 'dir_' + str(i))
        try:
            os.mkdir(my_path)
        except FileExistsError:
            print('Каталог {} уже существует'.format(my_path))
    under_menu()


def del_dirs(start=1, stop=10):
    # функция удаления директорий в диапазоне dir_1-dir9 в папке, где запущен скрипт
    for i in range(start, stop):
        my_path = os.path.join(os.getcwd(), 'dir_' + str(i))
        try:
            os.rmdir(my_path)
        except FileNotFoundError:
            print('Каталог {} НЕ существует'.format(my_path))
    under_menu()


def make_a_copy_work_file():
    # функция создания копии файла скрипта в папке, где запущен скрипт
    copy_path = os.path.join(os.getcwd(), ''.join(['copy_of_', os.path.basename(sys.argv[0])]))
    if os.path.exists(copy_path) is False:
        shutil.copy(sys.argv[0], copy_path)
        print('Создана копия исходного файла скрипта.\n{}'.format(copy_path))
    else:
        question = input('копия файла уже существует. Для перезаписи введите 1: ')
        if question == '1':
            shutil.copy(sys.argv[0], copy_path)
            print('Файл копии исходного скрипта перезаписан.\n{}'.format(copy_path))
        else:
            print('Файл копии не перезаписан.\n')
    under_menu()


def view_dirs():
    # функция просмотра содержимого папки, где запущен скрипт
    print('\nСодержимое каталога:')
    [print('{}'.format(i)) for i in sorted(os.listdir(os.getcwd()))]
    print()
    under_menu()


def exit():
    # функция выхода из программы
    print('\nСпасибо. Всего доброго')


def main_menu():
    user_choice = input('\nВыберите пункт меню:\n'
                        '1. Создать каталоги\n'
                        '2. Удалить созданные каталоги\n'
                        '3. Создать копию рабочего файла\n'
                        '4. Посмотреть содержимое папки\n'
                        '5. Выход из программы\n'
                        'Ваш выбор: ')
    check_input(user_choice)


def under_menu():
    # функция для выхода из программы без возврата в основное меню
    user_choice = input('Вернуться в главное меню? Для выхода из программы введите любой символ: ')
    if user_choice == '':
        main_menu()
    else:
        exit()


def check_input(user_choice):
    try:
        functions_dictionary(int(user_choice))
    except ValueError:
        print('\nВы должны ввести № пункта меню в ВИДЕ ЦИФРЫ. Повторите попытку\n')
        main_menu()
    except KeyError:
        print('\nТакого пунка в меню нет. Повторите попытку\n')
        main_menu()


def functions_dictionary(key):
    return dict(zip(range(1, 6), [make_dirs,
                                  del_dirs,
                                  make_a_copy_work_file,
                                  view_dirs,
                                  exit]))[key]()


main_menu()