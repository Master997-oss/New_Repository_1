import os, shutil
import sys



# Задача-1:
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


if __name__ == '__main__':
    try:
        a = float(input("a = "))
        b = float(input("b = "))
    except ValueError:
        print("Неверный формат данных - введите числа!!!")
    else:
        c = avg(a, b)
        print("Среднее геометрическое = {:.2f}".format(c))




# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html




# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_directory():
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), f"dir_{i}")
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print(f"Директория dir_{i} уже существует!")

def dell_directory():
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), f"dir_{i}")
        try:
            os.rmdir(dir_path)
        except FileNotFoundError:
            print(f"Директории dir_{i} не существует!")

if __name__ == '__main__':
    create_directory()
    dell_directory()




# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.


def list_directory():
    if __name__ == '__main__':
        for item in os.listdir(os.getcwd()):
            if os.path.isdir(item):
                print(item)
    else:
        for item in os.listdir(os.getcwd()):
            print(item)


if __name__ == '__main__':
    list_directory()



# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def create_main_copy():
    src_path = os.path.join(os.getcwd(), os.path.split(__file__)[1])
    des_path = os.path.join(os.getcwd(), "copy_" + os.path.split(__file__)[1])
    shutil.copy(src_path, des_path)

if __name__ == '__main__':
    create_main_copy()