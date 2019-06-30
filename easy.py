# используется исключительно для выполнения задания в категории normal


import os
import sys
import shutil
import re


def get_path(dir_name):
    return os.path.join(os.getcwd(), dir_name)

def make_dir():
    # функция создания директории по запросу
    dir_name = input('\nВведите название директории: ')
    if check_dir_name(dir_name):
        my_path = get_path(dir_name)
        try:
            os.mkdir(my_path)
            print('\nПапка успешно создана\n')
        except FileExistsError:
            print('\nНевозможно создать. Каталог\n{}\nуже существует\n'.format(my_path))
        action_arg = under_menu()
        return action_arg
    else:
        return True




def del_dir():
    # функция удаления директории по запросу
    dir_name = input('\nВведите название директории: ')
    if check_dir_name(dir_name):
        my_path = get_path(dir_name)
        try:
            os.rmdir(my_path)
            print('\nПапка успешно удалена\n')
        except FileNotFoundError:
            print('\nНевозможно удалить. Каталог\n{}\nНЕ существует\n'.format(my_path))
        action_arg = under_menu()
        return action_arg
    else:
        return True


def go_up():
    question = input('\nОстаться в текущем каталоге? Чтобы перейти на каталог выше:\n{}\n'
                     'Введите любой символ: '.format(os.path.dirname(os.getcwd())))
    if question != '':
        os.chdir(os.path.dirname(os.getcwd()))
        print('\nПереход осуществлен успешно. Текущее положение:\n{}\n'.format(os.getcwd()))
        result = view_dirs()
        return result
    else:
        print('\nПереход НЕ осуществлен. Текущее положение:\n{}\n'.format(os.getcwd()))

def change_dir():
    # функция смена директории по запросу
    result = go_up()
    if result is None:
        dir_name = input('\nВведите название директории для перехода: ')
        if check_dir_name(dir_name):
            my_path = get_path(dir_name)
            try:
                os.chdir(my_path)
                print('\nПереход осуществлен успешно. Текущее положение:\n{}\n'.format(my_path))
                result2 = go_up()
                if result2 is None:
                    pass
                else:
                    return result2
            except FileNotFoundError:
                print('\nНевозможно перейти. Каталог\n{} указан неверно\n'.format(my_path))
            action_arg = under_menu()
            return action_arg
        else:
            return True
    else:
        return result


def check_dir_name(dir_name):
    pattern = '^[a-zA-ZА-Яа-я0-9_]+$'
    try:
        re.search(pattern, dir_name).group(0)
        return True
    except AttributeError:
        print('Ошибка. Недопустимое имя каталога.')
        return False


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
    action_arg = under_menu()
    return action_arg


def view_dirs():
    # функция просмотра содержимого папки, где запущен скрипт
    print('\nСодержимое каталога:')
    [print('{}'.format(i)) for i in sorted(os.listdir(os.getcwd()))]
    print('\n_______________________________\n')
    action_arg = under_menu()
    return action_arg


def exit():
    # функция выхода из программы
    return False


def main_menu():
    return input('\nВыберите пункт меню:\n'
                        '1. Перейти в папку\n'
                        '2. Просмотреть содержимое текущей папки\n'
                        '3. Удалить папку\n'
                        '4. Создать папку\n'
                        '5. Выход из программы\n'
                        'Ваш выбор: ')


def under_menu():
    # функция для выхода из программы без возврата в основное меню
    user_choice = input('Вернуться в главное меню? Для выхода из программы введите любой символ: ')
    if user_choice == '':
        return True
    else:
        return False


def check_input(user_choice):
    try:
        action_arg = functions_dictionary(int(user_choice))
    except ValueError:
        print('\nВы должны ввести № пункта меню в ВИДЕ ЦИФРЫ. Повторите попытку\n')
        return True
    except KeyError:
        print('\nТакого пунка в меню нет. Повторите попытку\n')
        return True
    return action_arg


def functions_dictionary(key):
    action_arg = dict(zip(range(1, 6), [change_dir,
                                  view_dirs,
                                  del_dir,
                                  make_dir,
                                  exit]))[key]()
    return action_arg


# main_menu()