import os
import shutil
import sys


# Задача-1:
# Примечание: Если уже делали easy задание, то просто перенесите решение сюда.
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:

def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5

a = float(input("a = "))
b = float(input("b = "))
c = avg(a, b)
print("Среднее геометрическое = {:.2f}".format(c))


# Исправленная программа:
"""
Ошибки(номера строк): 22, 24, 25
"""

def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.

    Исключения:
        - ValueError: вычисление не возможно.
    """
    if a * b >= 0:
        return (a * b) ** 0.5
    else:
        raise ValueError("Невозможно определить среднее геометрическое "
                         "введенных чисел.")

try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError as err:
    print("Ошибка:", err, ". Проверьте введенные числа.")
except Exception as err:
    print("Ошибка:", err)



# ПРИМЕЧАНИЕ: Для решения задачи 2-3 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь "меню" выбора действия, в котором будут пункты:
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


from hw06_easy import create_directory, dell_directory, list_directory, create_main_copy


def change_dir(path):
    try:
        os.chdir(path)
        return 'Успешно перешли в папку: {}'.format(path)
    except FileNotFoundError:
        return ('dir_{} - папки не существует'.format(path))

def main_func ():
    answer =''
    while answer != '5':
        print('----------------------------------------')
        print('Текущая директория: ' + os.getcwd())
        answer = input('Выберите пункт меню:\n'
                       '1. Перейти в папку\n'
                       '2. Помотреть содержимое текущей папки\n'
                       '3. Удалить папку\n'
                       '4. Создать папку\n'
                       '5. Выход\n')
        if answer =='5':
            break
        if answer == '1':
            path_name = input('Укажите папку для перехода: ')
            print(create_main_copy(path_name))
        elif answer == '2':
            hw06_easy.list_directory()
        elif answer == '3':
            name = input('Введите имя удаляемой папки: ')
            hw06_easy.dell_directory(name)
        elif answer == '4':
            name = input('Введите имя новой папки: ')
            hw06_easy.create_directory(name)

if __name__ == '__main__':
    main_func()
