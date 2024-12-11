#Задача "Магические здания"
class House:            # Создание нового класса House

    def __init__(self, name, number_of_floors):          # Определение метода __init__ в классе House
        self.name = name                                 # c атрибутами объекта self.name и self.number_of_floors
        self.number_of_floors = number_of_floors

    def __len__(self):                      # Определение метода __len__ в классе House
        return self.number_of_floors        # возвращает кол-во этажей объекта

    def __str__(self):                      # Определение метода __str__ в классе House
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
                                            # возвращает строку с названием и этажностью объекта

h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)

print(str(h1))                               # Обращение к методу str для объекта h1 класса House
print(str(h2))                               # Обращение к методу str для объекта h2 класса House

print(len(h1))                               # Обращение к методу len для объекта h1 класса House
print(len(h2))                               # Обращение к методу len для объекта h2 класса House