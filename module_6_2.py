# Задача "Изменять нельзя получать":

class Vehicle:                                               # Родительский класс Vehicle и его атрибуты:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']   # список допустимых цветов транспорта

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner                                   # имя владельца (может меняться)
        self.__model = model                                 # модель (не может меняться)
        self.__engine_power = engine_power                   # мощность двигателя (не может меняться)
        self.__color = color                                 # цвет (может меняться только на допустимые)

    def get_model(self):                                     # метод get_mode
        print(f"Модель: {self.__model}")                     # возвращает строку: "Модель: <название модели транспорта>"

    def get_horsepower(self):                                # метод get_horsepower
        print(f"Мощность двигателя: {self.__engine_power}")  # возвращает строку: "Мощность двигателя: <мощность>"

    def get_color(self):                                     # метод get_color
        print(f"Цвет: {self.__color}")                       # возвращает строку: "Цвет: <цвет транспорта>"

    def print_info(self):                                    # метод print_info возвращает 4 строки:
        self.get_model()                                     # 1 строка: "Модель: <название модели транспорта>"
        self.get_horsepower()                                # 2 строка: "Мощность двигателя: <мощность>"
        self.get_color()                                     # 3 строка: "Цвет: <цвет транспорта>"
        print(f"Владелец: {self.owner}")                     # 4 строка: "Владелец: <имя>"


    def set_color(self, new_color):                          # метод set_color
        col = new_color.lower()
        if col in self.__COLOR_VARIANTS:                     # если новый цвет есть в списке допустимых цветов транспорта
            self.__color = col                               # то цвет меняется на новый
        else: print(f"Нельзя сменить цвет на {new_color}")   # иначе инфо о невозможности сменить цвет на желаемый

class Sedan(Vehicle):                                        # дочерний класс Sedan и его атрибуты:
    __PASSENGERS_LIMIT = 5                                   # число пассажиров

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue' )

vehicle1.print_info()                                        # Изначальные свойства

vehicle1.set_color('Pink')                                   # изменение свойств (метод)

vehicle1.set_color('BLACK')                                  # изменение свойств (метод)

vehicle1.owner = 'Vasyok'                                    # изменение свойств (присваивание)

vehicle1.print_info()                                        # новые свойства