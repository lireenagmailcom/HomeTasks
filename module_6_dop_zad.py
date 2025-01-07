# Задание "Они все так похожи"
import math                                           # импорт модуля math

class Figure:                                         # Родительский класс Figure
    sides_count = 0                                   # атрибуты класса Figure: sides_count = 0

    def __init__(self, color, *sides):                # метод __init__ с параметрами объекта: цвет и список сторон (int)
        self.filled = False                           # атрибут filled = False

        if self.__is_valid_color(*color):             # если цвет в формате RGB корректный, то
            self.__color = list(color)                # объекту присваивается этот цвет,
        else: self.__color = [0, 0, 0]                # иначе объекту присваивается черный цвет,

        if self._is_valid_sides(*sides):              # если количество сторон корректно, то
            self._sides = list(sides)                 # сторонам объекта присваиваются эти значения
        else:                                         # иначе объекту присваиваются все стороны равные 1
            self._sides = [1 for _ in range(self.sides_count)]

    def get_color(self):                              # метод get_color возвращает цвет объекта в формате RGB
        return self.__color

    def __corr(self,num):                             # ф-ция __corr проверяет, является ли число целым от 0 до 255
        return isinstance(num, int) and num >= 0 and num <= 255

    def __is_valid_color(self, r, g, b):              # метод __is_valid_color проверяет корректность параметров r, g, b
        return self.__corr(r) and self.__corr(g) and self.__corr(b)   # каждый параметр должен быть целым числом от 0 до 255

    def set_color(self, r,g,b):                       # метод set_color принимает параметры r, g, b - числа
        if self.__is_valid_color(r,g,b):              # если введены корректные данные, то цвет изменится,
            self.__color = [r, g, b]                  # а если введены некорректные данные, то цвет остаётся прежним

    def _is_valid_sides(self, *new_sides):            # метод _is_valid_sides принимает неограниченное кол-во новых сторон,
        if len(new_sides) != self.sides_count:        # если кол-во новых сторон не совпадает с текущим числом сторон,
            return False                              # то выход из функции с результатом False
        for i in range(len(new_sides)):               # иначе в цикле по новым сторонам проверяется их положительность и тип int
            if new_sides[i] <= 0 or not isinstance(new_sides[i], int):  # если число не положительное или не целое
                return False                          # то выход из функции с результатом False
        return True                                   # иначе выход из функции с результатом True

    def get_sides(self):                              # метод get_sides возвращает значения атрибута _sides
       return self._sides

    def __len__(self):                                # метод __len__ возвращает периметр фигуры
       return sum(self._sides)

    def set_sides(self, *new_sides):                  # метод set_sides(self, *new_sides) должен принимать новые стороны,
        if self._is_valid_sides(*new_sides):          # если результат метода is_valid_sides верен,
            self._sides = list(new_sides)             # то старые значения меняются на новые, иначе - не меняются


class Circle(Figure):                                 # дочерний класс Circle(Figure)
    sides_count = 1                                   # фигура с 1 (одной) стороной

    def __init__(self, color, *sides):                # метод __init__ класса Circle(Figure)
        super().__init__(color, *sides)        # атрибуты наследуются из родительского класса
        self.radius = sides[0] / (2 * math.pi)        # радиус = сторона / (2 * math.pi)

    def get_square(self):                             # метод get_square возвращает площадь круга
        return  math.pi * (self.radius ** 2)


class Triangle(Figure):                               # дочерний класс Triangle(Figure)
    sides_count = 3                                   # фигура с 3 (тремя) сторонами

    def _is_valid_sides(self, *new_sides):            # метод _is_valid_sides с параметром - список новых сторон (int)
        if not super()._is_valid_sides(*new_sides):   # вызывается одноименный метод из родительского класса
            return False                              # выход и возврат False, если результат проверки отрицательный
        if new_sides[0] >= new_sides[1] + new_sides[2]: return False   # проверка условия существования 3-угольника
        if new_sides[1] >= new_sides[0] + new_sides[2]: return False   # проверка условия существования 3-угольника
        if new_sides[2] >= new_sides[1] + new_sides[0]: return False   # проверка условия существования 3-угольника
        return True

    def get_square(self):                             # метод get_square возвращает площадь треугольника
        a = self._sides                               # а - список сторон треугольника
        p = self.__len__() / 2                        # р - 1/2 периметра треугольника
        s = p * (p - a[0]) * (p - a[1]) * (p - a[2])  # s - квадрат площади треугольника по формуле Герона
        return math.sqrt(s)                           # возвращается площадь треугольника

class Cube(Figure):                                   # дочерний класс Cube(Figure)
    sides_count = 12                                  # фигура с 12 ребрами

    def __init__(self, color, *sides):                # метод __init__ с параметрами цвет (RGB) и список сторон (целые числа)
        super().__init__(color, *sides)        # обращаемся к методу __init__ родительского класса с теми же параметрами
        if len(self._sides) == 1:                     # если длина списка сторон = 1, то все ребра куба равны
            self._sides = [self._sides[0] for _ in range(self.sides_count)]  # единственному элементу списка

    def _is_valid_sides(self, *new_sides):            # метод _is_valid_sides с параметром - список новых сторон (int)
        if len(new_sides) == 1 and isinstance(new_sides[0], int) and new_sides[0] > 0: # если список 1-элементный и
            return True                               # этот элемент является целым и положительным, то True
        if len(new_sides) != 12:                      # если список не 12-элементный, то False
            return False
        if not (isinstance(new_sides[0], int) and new_sides[0] > 0): # если первый элемент 12-элементного списка
            return False                              # не является целым и положительным, то False
        for i in range(11):                           # проверка в цикле по элементам списка: если элемент от 2-го до 12-го
            if not (isinstance(new_sides[i+1], int) and new_sides[i+1] == new_sides[0] ): # не является целым или != 1-му,
                return False                                                              #  то False
        return True                                   # возвращает True

    def set_sides(self, *new_sides):                  # метод set_sides с параметрами значения новых сторон
        super().set_sides(*new_sides)                 # обращаемся к методу set_sides родительского класса с теми же параметрами
        if len(self._sides) == 1:                     # если список 1-элементный, то всем ребрам куба
            self._sides = [self._sides[0] for _ in range(self.sides_count)] # присваивается значение этого элемента

    def get_volume(self):                             # метод get_volume, который
        return self._sides[0] ** 3                    # возвращает объем куба


circle1 = Circle((200, 200, 100), 10)    # создание окружности с цветом (200, 200, 100) и длиной 10

cube1 = Cube((222, 35, 130), 6)          # создание куба с цветом (222, 35, 130) и ребрами 6

circle1.set_color(55, 66, 77)                # проверка на изменение цвета: изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15)                 # проверка на изменение цвета: не изменится

print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)             # проверка на изменение сторон: не изменится

print(cube1.get_sides())

circle1.set_sides(15)                                 # проверка на изменение сторон: изменится

print(circle1.get_sides())

print(f"Длина окружности = {(circle1.get_sides())[0]}") # периметр, т.е. длина окружности

print(f"Объем куба = {cube1.get_volume()}")           # объём (куба)