#Задача "Developer - не только разработчик":
class House:            # Создание нового класса House

    def __init__(self, name, number_of_floors):          # Определение метода __init__ в классе House
        self.name = name                                 # c атрибутами объекта self.name и self.number_of_floors
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):                          # Определение метода go_to в классе House
        print(f"{self.name}, этажность: {self.number_of_floors}")        # имя и этажность заданного объекта
        print("Подъем на этаж:", new_floor)                         # подъем на заданный этаж
        if new_floor > self.number_of_floors or new_floor < 1: # если на такой этаж нельзя подняться,
                print("Такого этажа не существует")                      # то сообщение об этом и выход
                return
        for i in range(new_floor):                                  # иначе цикл по этажам от 1 до заданного
            print(i+1)

h1 = House('ЖК Горский', 18)                    # Создание объекта h1 класса House

h2 = House('Домик в деревне', 2)                # Создание объекта h2 класса House

h1.go_to(3)                                # Обращение к методу go_to для объекта h1 класса House

h2.go_to(5)                                # Обращение к методу go_to для объекта h1 класса House
