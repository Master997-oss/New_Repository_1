#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


from random import randint


def generation_unique_numb(counting, min_bound, max_bound):
    if counting > max_bound - min_bound + 1:
        raise ValueError('Некоректно введены параметры!')
    dropout = []
    while len(dropout) < counting:
        new = randint(min_bound, max_bound)
        if new not in dropout:
            dropout.append(new)
    return dropout


class Keg:
    __num = None

    def __init__(self):
        self.__num = randint(1, 90)

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return str(self.__num)


class Card:
    __rows = 3
    __column = 9
    __nums_in_row = 5
    __emptynumber = 0
    __crossedoutnumber = -1
    __data = None

    def __init__(self):
        uniques_counting = self.__nums_in_row * self.__rows
        uniques = generation_unique_numb(uniques_counting, 1, 90)

        self.__data = []
        for i in range(0, self.__rows):
            tmp = sorted(uniques[self.__nums_in_row * i: self.__nums_in_row * (i + 1)])
            empty_nums_counting = self.__column - self.__nums_in_row
            for j in range(0, empty_nums_counting):
                index = randint(0, len(tmp))
                tmp.insert(index, self.__emptynumber)
            self.__data += tmp

    def __str__(self):
        separator = '**************************'
        ret = separator + '\n'
        for index, num in enumerate(self.__data):
            if num == self.__emptynumber:
                ret += '  '
            elif num == self.__crossedoutnumber:
                ret += ' -'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)

            if (index + 1) % self.__column == 0:
                ret += '\n'
            else:
                ret += ' '

        return ret + separator

    def __contains__(self, item):
        return item in self.__data

    def cross_num(self, num):
        for index, item in enumerate(self.__data):
            if item == num:
                self.__data[index] = self.__crossedoutnumber
                return
        raise ValueError(f'Числа нет в карточке: {num}')

    def closed(self) -> bool:
        return set(self.__data) == {self.__emptynumber, self.__crossedoutnumber}


class Game:
    __usercard = None
    __compcard = None
    __kegs = []
    __numkegs = 90
    __gameover = False

    def __init__(self):
        self.__usercard = Card()
        self.__compcard = Card()
        self.__kegs = generation_unique_numb(self.__numkegs, 1, 90)

    def play_round(self) -> int:
        keg = self.__kegs.pop()
        print(f'Новый бочонок: {keg} (осталось {len(self.__kegs)})')
        print(f'----- Ваша карточка ------\n{self.__usercard}')
        print(f'-- Карточка компьютера ---\n{self.__compcard}')

        useranswer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if useranswer == 'y' and not keg in self.__usercard or \
           useranswer != 'y' and keg in self.__usercard:
            return 2

        if keg in self.__usercard:
            self.__usercard.cross_num(keg)
            if self.__usercard.closed():
                return 1
        if keg in self.__compcard:
            self.__compcard.cross_num(keg)
            if self.__compcard.closed():
                return 2
        return 0



if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_round()
        if score == 1:
            print('Вы победили:)')
            break
        elif score == 2:
            print('Вы проиграли:(')
            break