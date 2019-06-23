# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

names = ['Ivan', 'German', 'Vladimir', 'Aleksey', 'Dmitriy']
money = [35000, 1000000, 99999999, 49000, 9000]
work_table = dict(zip(names, money))

def zp_file(work_dictionary: dict, max_money=50000, file_name='salary.txt'):
    with open(file_name, 'w+', encoding='utf-8') as file:
        for key, arg in work_dictionary.items():
            if arg <= max_money:
                file.write('{} - {}\n'.format(key, arg))

zp_file(work_table)