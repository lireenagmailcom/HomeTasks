#Задача "История строительства":

class House:              # Создание нового класса House
    houses_history = []   # Определение переменной cls.houses_history

    def __new__(cls, *args, **kwargs):                # Определение метода __new__ в классе House
        cls.houses_history.append(args[0])            # в конец списка houses_history добавляется эл-т args[0], т.е. name
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):       # Определение метода __init__ в классе House
        self.name = name                              # c атрибутами объекта self.name и self.number_of_floors
        self.number_of_floors = number_of_floors


    def __del__(self):                                # Определение метода __del__ в классе House
        print(f"{self.name} снесён, но он останется в истории") # список houses_history не меняется

#Пример выполнения программы:

h1 = House('ЖК Эльбрус', 10)        # создание объекта h1
print(House.houses_history)                             # список houses_history содержит 1 эл-т

h2 = House('ЖК Акация', 20)         # создание объекта h2
print(House.houses_history)                             # список houses_history содержит 2 эл-та

h3 = House('ЖК Матрёшки', 20)       # создание объекта h3
print(House.houses_history)                              # список houses_history содержит 3 эл-та

del h2                                                   # Удаление объекта h2

del h3                                                   # Удаление объекта h3

print(House.houses_history)                              # список houses_history не меняется




#Вывод на консоль:

#['ЖК Эльбрус', 'ЖК Акация']

#['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

#ЖК Акация снесён, но он останется в истории

#ЖК Матрёшки снесён, но он останется в истории

#['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

#ЖК Эльбрус снесён, но он останется в истории



#Примечания:

#Более подробно о работе метода __new__ можно узнать здесь.
#В методе __new__ можно обращаться к атрибутам текущего класса при помощи параметра cls.
