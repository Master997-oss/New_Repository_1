# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Pers:
    def __init__(self, surname, name, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        full_name = self.surname + " " + self.name + " " + self.patronymic
        return full_name

    def get_shortname(self):
        print(f"{self.surname.title()} {self.name[0].upper()}.{self.patronymic[0].upper()}")


class Student(Pers):
    def __init__(self, surname, name, patronymic, class_num, mother, father):
        super().__init__(surname, name, patronymic)
        self.mother = mother
        self.father = father
        self.class_num = class_num

    def get_parents(self):
        print(f"Маму зовут: {self.surname}а {self.mother}\n"
              f"Отца зовут: {self.surname}a {self.father}")


class Teacher(Pers):
    def __init__(self, surname, name, patronymic, subject):
        super().__init__(surname, name, patronymic)
        self.subject = subject


class Class_rooms():
    def __init__(self, class_num, subjects, teachers):
        self.class_num = class_num
        self.subjects = {subjects: teachers}


classes = [Class_rooms("5A", "Математика", "Спиридонов Георгий Иванович"),
           Class_rooms("6Б", "Физика", "Клементьев Инакентий Петрович"),
           Class_rooms("7В", "Русский язык", "Агапова Раиса Васильевна")]

teachers = [Teacher("Спиридонов", "Георгий", "Иванович", "Математика"),
            Teacher("Баранов", "Кирилл", "Владимирович", "Физкультура"),
            Teacher("Клементьев", "Инакентий", "Петрович", "Физика"),
            Teacher("Агапова", "Раиса", "Васильевна", "Русский язык")]

students = [Student("Иванов", "Иван", "ИМаксимович", "1Г", "Кристина", "Максим"),
            Student("Петров", "Пётр", "Андреевич", "6Б", "Анна", "Андрей"),
            Student("Татаринов", "Рафаэль", "Аликович", "5А", "Людмила", "Алик"),
            Student("Николаев", "Эдуард", "Сергеевич", "6А", "Сергей", "Сергей"),
            Student("Садомитов", "Олег", "Ольгович", "11Б", "Ольга", "Ольг")]


schoolchild_name = input("Введите ФИО интересующего ученика: ")
for schoolchild in students:
    if schoolchild.get_full_name() == schoolchild_name:
        schoolchild.get_parents()
        break
else:
    print("Такого ученика нет в школе")