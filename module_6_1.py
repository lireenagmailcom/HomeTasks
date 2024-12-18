#Задача "Съедобное, несъедобное":

class Animal:                                               # Родительский класс  Animal
    def __init__(self, name, alive = True, fed = False):    # его атрибуты: name, alive = True, fed = False
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):                                    # метод eat с параметром food
        if food.is_edible():                                # если food является edible,
            self.fed = True                                 # то атрибут fed принимает значение True и
            print(f"{self.name} съел {food.name}")          # выводится строка {кто} съел {что}
        else:                                               # иначе
            print(f"{self.name} не стал есть {food.name}")  # выводится строка {кто} не стал есть {что}
            self.alive = False                              # и атрибут alive принимает значение False


class Mammal(Animal):                                       # дочерний класс Mammal
    pass

class Predator(Animal):                                     # дочерний класс Predator
    pass


class Plant:                                                # Родительский класс Plant
    def __init__(self, name, edible = False):               # его атрибуты: name, edible = False
        self.name = name
        self.edible = edible

    def is_edible(self):                                    # метод is_edible
        return self.edible


class Flower(Plant):                                        # дочерний класс Flower
    def __init__(self, name, edible=False):                 # и его атрибуты name, edible=False
        super().__init__(name, edible=edible)
        self.edible = False


class Fruit(Plant):                                         # дочерний класс Fruit
    def __init__(self, name, edible = True):                # и его атрибуты name, edible=False
        super().__init__(name, edible=edible)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')



print(a1.name)

print(p1.name)



print(a1.alive)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(a1.alive)

print(a2.fed)


#Вывод на консоль:

#Волк с Уолл-Стрит

#Цветик семицветик

#True

#False

#Волк с Уолл-Стрит не стал есть Цветик семицветик

#Хатико съел Заводной апельсин

#False

#True

