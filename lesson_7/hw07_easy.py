import math


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# class Triangle:
#     def __init__(self, a, b, c):              # данная функция вычисляет длину стороны по координатам точек
#
#         def sideLen(d1, d2):
#             return math.sqrt((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2)
#         self.a = a
#         self.b = b
#         self.c = c
#         self.ab = sideLen(self.a, self.b)        # вычисление длины стороны ab
#         self.bc = sideLen(self.b, self.c)        # вычисление длины стороны bc
#         self.ca = sideLen(self.c, self.a)        # вычисление длины стороны ca
#
#
#     def P_Triangle(self):  # вычисление периметра треугольника
#         return self.ab + self.bc + self.ca
#
#     def H_Triangle(self):  # вычисление высоты треугольника
#         return self.S_Triangle() / (self.ab / 2)
#
#     def S_Triangle(self):                           # вычисление площади треугольника(формула Герона)
#         S_p = self.P_Triangle() / 2
#         return math.sqrt(S_p
#                          * (S_p - self.ab)
#                          * (S_p - self.bc)
#                          * (S_p - self.ca))
#
#
# triangle_1 = Triangle((5, 4), (10, 11), (0, 15))
#
# print(triangle_1.H_Triangle())
# print(triangle_1.P_Triangle())
# print(triangle_1.S_Triangle())





# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezoid:
    def __init__(self, a, b, c, d):      # данная функция вычисляет длину стороны согласно координатам точек
        def sideLen(d1, d2):
            return math.sqrt((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2)

        def S_Triangle(len1, len2, len3):
            S_p = (len1 + len2 + len3) / 2

            return math.sqrt(S_p
                             * (S_p - len1)
                             * (S_p - len2)
                             * (S_p - len3))

        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.ab = sideLen(self.a, self.b)
        self.bc = sideLen(self.b, self.c)
        self.cd = sideLen(self.c, self.d)
        self.da = sideLen(self.d, self.d)
        self.diag_ac = sideLen(self.c, self.a)
        self.diag_bd = sideLen(self.b, self.d)
        self.P = self.ab + self.bc + self.cd + self.da

        # представление трапеции в виде 2-х треугольников, сложение площадей этих 2-х треугольников
        self.S = S_Triangle(self.ab, self.diag_bd, self.da) + S_Triangle(self.diag_bd, self.bc, self.cd)

    def isIsoscelesTrapezoid(self):
        if self.diag_ac == self.diag_bd:
            return True
        return False

