from datetime import datetime


"""
Предметная область – магазин. Разработать класс Shop,
описывающий работу магазина продуктов. Разработать класс
Products, продукт описывается следующими параметрами:
уникальный идентификатор, название продукта, стоимость,
количество. Разработать класс FruitProduct на базе класс Product,
фрукт характеризуется параметрами: страна изготовителя, срок
годности.
"""



class Shop():
    def __init__(self, shop_name, num_pos):
        self.shop_name = shop_name
        self.num_pos = num_pos
        self.magazin = []

    def addP(self, *addp):
        for ap in addp:
            self.magazin.append(ap) if len(self.magazin) < self.num_pos else print(f"Товар не добавлен! Ассортимент магазина ограничен позициями в кол-ве: {self.num_pos} ")

    def ast_best_before(self, date):
        print(f"\nАссортимент свежих товаров магазина: {self.shop_name}")
        for pr in self.magazin:
            pr.date_exp(date)

    @property
    def assortiment(self):
        print(f"\nАссортимент магазина {self.shop_name}" if self.magazin else f"В магазине нет продуктов:(")
        for pr in self.magazin:
            pr.info()

    @property
    def edit_val_assortiment(self):
        print(f"\nОстаток товара магазина {self.shop_name}" if self.magazin else f"В магазине нет продуктов:(")
        for pr in self.magazin:
            pr.info()
            p_new = input(f"Остаток товара на данный момент: {pr.val}\nВведите новое значение при необходимости внести изменения: ")
            if p_new:
                pr.val = int(p_new)
                print(f"Актуальный остаток товара: {pr.val}")

    @property
    def dell_assortiment(self):
        self.magazin = []
        print(f"\nАссортимент магазина очищен")


class Products(Shop):
    #__slots__ = ("self", "p_id", "p_name", "p_price", "p_val", "p_country", "p_date")
    def __init__(self, p_id, p_name, p_price, p_val):
        self.p_type = "Хозяйственные товары"
        self.p_id = p_id
        self.p_name = p_name
        self.p_price = p_price
        self.p_val = p_val

    def info(self):
        print(f"ID: {self.p_id:>4}  Товар: {self.p_name:>10}  Категория: {self.p_type:>15}  Цена: {self.p_price:>5}")

    @property
    def val(self):
        return self.p_val

    @val.setter
    def val(self, val):
        self.p_val = val

    def date_exp(self, date_exp):
        print(f"Товар {self.p_name:15} без срока хранения")

class FruitProduct(Products):
    def __init__(self, p_id, p_name, p_price, p_val, p_country, p_date):
        super().__init__(p_id, p_name, p_price, p_val)
        self.p_type = "Фрукты"
        self.p_country = p_country
        self.p_date = p_date

    def date_exp(self, date_exp):
        if datetime.strptime(date_exp, "%d/%m/%Y") > datetime.strptime(self.p_date, "%d/%m/%Y"):
            print(f"Товар {self.p_name:15} годен")
        else:
            print(f"Товар {self.p_name:15} просрочен, его срок годности истек! {self.p_date}")


    def magazin():
        s = Shop("ЛЕНТА", 4)
        f1 = Products(500, "Сковорода", 1600, 50)
        f2 = Products(510, "Банка", 60, 20)
        f3 = Products(520, "Кастрюля", 90, 30)
        f4 = Products(490, "Набор ложек", 50, 10)
        f5 = Products(490, "Набор вилок", 40, 10)
        f6 = Products(490, "Набор ножей", 100,20)
        fp1 = FruitProduct(510, "Апельсины", 200, 110, "Турция", "01/12/2023")
        fp2 = FruitProduct(550, "Финики", 100, 25, "Египет", "01/11/2023")
        fp3 = FruitProduct(550, "<Бананы>", 180, 60, "Мороко", "01/11/2023")
        fp4 = FruitProduct(550, "Кокосы", 150, 50, "Ямайка", "01/12/2024")
        fp5 = FruitProduct(550, "Манго", 120, 20, "Тайланд", "01/11/2023")
        fp6 = FruitProduct(550, "Авокадо", 160, 40, "Тайланд", "01/11/2023")
        fp7 = FruitProduct(550, "Ананасы", 200, 20, "Ямайка", "01/11/2023")


        s.addP(f1)
        s.addP(f6, fp1, fp2, fp3, fp4, fp5, fp6, fp7, f4, f5, f6, f2, f3, f1)
        s.assortiment
        s.ast_best_before("31/12/2023")
        s.edit_val_assortiment
        s.dell_assortiment
        s.assortiment


if __name__ == "__main__":
    magazin()