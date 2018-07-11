# Задача-1:# Дан список, заполненный произвольными целыми числами, получите новый список,# элементами которого будут квадратные корни элементов исходного списка,# но только если результаты извлечения корня не имеют десятичной части и# если такой корень вообще можно извлечь# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]list_1 = [2, -5, 8, 9, -25, 25, 4, -100, 100, 0]list_2 = []for i in list_1:    n = 0    if i > 0:        while abs(i) > n ** 2:            n += 1        if abs(i) == n ** 2:            list_2.append(n)print(list_2)print('\n_________________________________________\n')# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.# Склонением пренебречь (2000 года, 2010 года)day = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',       'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое',       'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье',       'двадцать четвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое',       'двадцать девятое', 'тридцатое', 'тридцать первое']month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',         'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']date = input('Введите необходимую дату в формате  dd.mm.yyyy (например: 02.11.2013):\n')day_number = date.split('.')print('{} {} {} года.'.format(day[int(day_number[0]) - 1], month[int(day_number[1]) - 1], int(day_number[2])))print('\n_________________________________________\n')# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами# в диапазоне от -100 до 100. В списке должно быть n - элементов.# Подсказка:# для получения случайного числа используйте функцию randint() модуля randomimport randomn = int(input('Введите количество необходимых элементов списка случайных чисел: \n'))random_list = []for i in range(n):    random_list.append(random.randrange(-100, 100))print(random_list)print('\n_________________________________________\n')# Задача-4: Дан список, заполненный произвольными целыми числами.# Получите новый список, элементами которого будут:# а) неповторяющиеся элементы исходного списка:# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]# б) элементы исходного списка, которые не имеют повторений:# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]import randomrandom_list = []result_a = []result_ab = []result_b = []for i in range(random.randrange(5, 15)):    random_list.append(random.randrange(0, 9))result_a = list(set(random_list))for i in random_list:    result_ab.append(i)    while result_ab.count(i) == 1:        break    else:        result_ab.pop()for i in random_list:    if random_list.count(i) == 1:        result_b.append(i)print('А теперь давайте посмотрим на результаты: \nнаш случайный список: \n{}\nнаш результат неповторяющихся значений'      ' элементов списка: \n{}\nего другой вариант с гарантией сохранения порядка элементов:\n{}\nнаш список'      ' с элементами, которые изначально не имели повторений:\n{}\n'      'Спасибо за внимание'.format(random_list, result_a, result_ab, result_b))