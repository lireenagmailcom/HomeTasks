#Задача "Нужно больше этажей":

class House:            # Создание нового класса House

    def __init__(self, name, number_of_floors):          # Определение метода __init__ в классе House
        self.name = name                                 # c атрибутами объекта self.name и self.number_of_floors
        self.number_of_floors = number_of_floors

    def __len__(self):                      # Определение метода __len__ в классе House
        return self.number_of_floors        # возвращает кол-во этажей объекта

    def __str__(self):                      # Определение метода __str__ в классе House
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
                                            # возвращает строку с названием и этажностью объекта

    def __eq__(self, other):                # Определение метода __eq__ в классе House
        if isinstance(other, int): a = other          # other указывает на объект типа int
        elif isinstance(other, House): a = len(other) # other указывает на объект типа House
        else: return NotImplemented                   # other указывает на объект иного типа
        return self.number_of_floors == a   # возвращает True, если этажность одинаковая, и False в противном случае

    def __ne__(self, other):                # Определение метода __ne__ в классе House
        if isinstance(other, int): a = other          # other указывает на объект типа int
        elif isinstance(other, House): a = len(other) # other указывает на объект типа House
        else: return NotImplemented                   # other указывает на объект иного типа
        return self.number_of_floors != a   # возвращает False, если этажность одинаковая, и True в противном случае


    def __lt__(self, other):                # Определение метода __lt__ в классе House
        if isinstance(other, int): a = other          # other указывает на объект типа int
        elif isinstance(other, House): a = len(other) # other указывает на объект типа House
        else: return NotImplemented                   # other указывает на объект иного типа
        return self.number_of_floors < a    # возвращает True, если self ниже, чем other

    def __le__(self, other):                # Определение метода __le__ в классе House
        if isinstance(other, int): a = other          # other указывает на объект типа int
        elif isinstance(other, House): a = len(other) # other указывает на объект типа House
        else: return NotImplemented                   # other указывает на объект иного типа
        return self.number_of_floors <= a   # возвращает True, если self не выше, чем other

    def __ge__(self, other):                # Определение метода __ge__ в классе House
        if isinstance(other, int): a = other          # other указывает на объект типа int
        elif isinstance(other, House): a = len(other) # other указывает на объект типа House
        else: return NotImplemented                   # other указывает на объект иного типа
        return self.number_of_floors >= a   # возвращает True, если self не ниже, чем other

    def __gt__(self, other):                # Определение метода __gt__ в классе House
        if isinstance(other, int): a = other          # other указывает на объект типа int
        elif isinstance(other, House): a = len(other) # other указывает на объект типа House
        else: return NotImplemented                   # other указывает на объект иного типа
        return self.number_of_floors > a    # возвращает True, если self выше, чем other

    def __add__(self, other):               # Определение метода __add__ в классе House
        if isinstance(other, int): a = other          # other указывает на объект типа int
        elif isinstance(other, House): a = len(other) # other указывает на объект типа House
        else: return NotImplemented                   # other указывает на объект иного типа
        self.number_of_floors += a          # этажность self увеличивается на other/len(other)
        return self                         # возвращает self

    def __radd__(self, other):              # Определение метода __radd__ в классе House
        return self.__add__(other)          # возвращает self.__add__(other)

    def __iadd__(self, other):              # Определение метода __iadd__ в классе House
        return self.__add__(other)          # возвращает self.__add__(other)

h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)

print(h1)

print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__

print(h1)

print(h1 == h2)

h1 += 10 # __iadd__

print(h1)

h2 = 10 + h2 # __radd__

print(h2)

print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__