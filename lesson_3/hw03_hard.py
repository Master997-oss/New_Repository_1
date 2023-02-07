# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y



equation = 'y = -12x + 11111140.2121'

x = 5.2

res = equation.split(' ')

first_name = str(res[2])

res[2] = first_name[:-1]

y = float(res[2]) * x + float(res[4])

print(y)



# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'


date = input('Введите дату в правильном формате dd.mm.yyyy: ')

chn_date = date.split('.')

chn_day = int(chn_date[0])

chn_month = int(chn_date[1])

chn_year = int(chn_date[2])

month_size = [1, 3, 5, 7, 8, 10, 12]

if len(chn_date[0]) != 2 or len(chn_date[1]) != 2 or len(chn_date[2]) != 4:

    print('Не корректен формат даты')

elif chn_day > 31 or chn_day < 1:

    print('Введён не корректный день')

elif chn_month > 12 or chn_month < 1:

    print('Введён не корректный месяц')

elif chn_year > 9999 or chn_year < 1:

    print('Введён не корректный год')

elif chn_month not in month_size and chn_day > 30:

    print('Введён не корректный день')

else:

    print('Дата введена корректно: ', date)



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

n = 10

zapros_etazh = 1

zapros_komnata = 1

otvet_etazh = 0

otvet_komnata = None

while n > 0:

    for current_etazh in range(zapros_etazh):

        otvet_etazh += 1

    for current_room in range(zapros_komnata):

        n -= 1

    if n == 0:

        otvet_komnata = current_komnata + 1

        break

    if n == 0:

        break

zapros_etazh += 1

zapros_komnata += 1

print(otvet_etazh, otvet_komnata)
