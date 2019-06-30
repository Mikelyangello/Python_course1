# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3


import os
import sys
import shutil


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (с подтверждением операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    # функция создания каталога в рабочей директории
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def make_a_copy_file():
    # функция создания копии файла скрипта в папке, где запущен скрипт
    if not dir_name:
        print("Необходимо указать полное имя файла вторым параметром")
        return
    user_file_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isfile(user_file_path):
        copy_path = os.path.join(os.getcwd(), ''.join(['copy_of_', dir_name]))
        if os.path.isfile(copy_path) is False:
            shutil.copy(user_file_path, copy_path)
            print('Создана копия исходного файла скрипта: {}.\n'
                  'Новая копия располагается:\n{}'.format(dir_name, copy_path))
        else:
            question = input('копия файла уже существует. Для перезаписи введите 1: ')
            if question == '1':
                shutil.copy(user_file_path, copy_path)
                print('\nФайл копии исходного скрипта\n{}\nперезаписан в директории:\n{}\n'.format(dir_name, copy_path))
            else:
                print('\nФайл копии не перезаписан.\n')
    else:
        print('\nфайла: \n{}\nНЕ существет, или адрес указан неверно.\n'
              'При наличии пробела в названии папки заключайте весь путь в двойные кавычки{}'
              ''.format(user_file_path, '""'))


def del_file():
    # функция удаления файла скрипта в папке, где запущен скрипт
    if not dir_name:
        print("Необходимо указать полное имя файла вторым параметром")
        return
    user_file_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isfile(user_file_path):
        question = input('Вы уверены, что хотите удалить файл \n{}\nи все его содержимое?\nОперация безвозвратная.\n'
                         'Для подтверждения введите "ДА": '.format(dir_name))
        if question == "ДА":
            os.remove(user_file_path)
            print('\nФайл {} успешно удален.\n'.format(dir_name))
        else:
            print('\nФайл {} НЕ удален.\n'.format(dir_name))
    else:
        print('Данного файла \n{}\nне существует или путь указан неправильно.'.format(dir_name))


def change_dir():
    pass
    if not dir_name:
        print("Необходимо вторым параметром указать имя директории или полный путь до нее")
        return
    if os.path.isdir(dir_name):
        os.chdir(dir_name)
        print('Директория изменена на \n{}'.format(os.getcwd()))
    else:
        print('Такой директории не существует. Проверьте правильность указанного пути:\n{}\nТекущий путь: \n{}\n'
              'при наличии пробела в имени папки, заключите весь путь в двойные кавычки. Например: \n{}'
              ''.format(os.path.abspath(dir_name), os.getcwd(), r'"C:\\Programm Files\Python\Nash kurs\Zanyatie-5"'))


def view_dir_path():
    # функция просмотра пути, где запущен скрипт
    print('\nТекущий путь рабочей папки:')
    print('_______________________________\n{}\n_______________________________\n'.format(os.getcwd()))


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": make_a_copy_file,
    "rm": del_file,
    "cd": change_dir,
    "ls": view_dir_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

print('\n**********************************************************\n')