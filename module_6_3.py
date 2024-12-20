# Задача "Ошибка эволюции":

import random

class Animal:                                               # Родительский класс  Animal
    live = True                                             # атрибут класса live = True
    sound = None                                            # атрибут класса sound = None
    _DEGREE_OF_DANGER = 0                                   # атрибут класса _DEGREE_OF_DANGER = 0

    def __init__(self, speed):                              # метод __init__ инициализация экземпляра
        self.speed = speed                                  # атрибут экземпляра speed
        self._cords = [0, 0, 0]                             # атрибут экземпляра _cords

    def move(self, dx, dy, dz):                             # метод move с координатами dx, dy, dz
        self._cords[0] += self.speed * dx                   # переопределение координаты dx
        self._cords[1] += self.speed * dy                   # переопределение координаты dy
        if self._cords[2] + self.speed * dz >= 0:           # если переопределенная координата dz неотрицательная
            self._cords[2] += self.speed * dz               # то переопределение координаты dz
        else: print("It's too deep, i can't dive :(")       # иначе вывод сообщения и координата не переопределяется

    def get_cords(self):                                    # метод get_cords выводит координаты
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):                                       # метод attack выводит
        if self._DEGREE_OF_DANGER < 5:                      # сообщение о миролюбии, если _DEGREE_OF_DANGER < 5
            print("Sorry, i'm peaceful :)")
        else: print("Be careful, i'm attacking you 0_0")    # иначе вывод сообщения об атаке

    def speak(self):                                        # метод speak выводит
        print(self.sound)                                   # запись звука, издаваемого экземпляром класса


class Bird(Animal):                                         # дочерний класс Bird(Animal)
    beak = True                                             # атрибут класса: наличие клюва

    def lay_eggs(self):                                     # метод lay_eggs
        rnd = random.randint(1, 4)                    # генерация случайного числа от 1 до 4
        print(f"Here are(is) {rnd} eggs for you")           # вывод сообщения о числе яиц


class AquaticAnimal(Animal):                                # дочерний класс AquaticAnimal(Animal)
    _DEGREE_OF_DANGER = 3                                   # атрибут класса _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):                                  # метод dive_in
        self._cords[2] -= int(self.speed * abs(dz) / 2)     # переопределяет координату dz


class PoisonousAnimal(Animal):                              # дочерний класс PoisonousAnimal(Animal)
    _DEGREE_OF_DANGER = 8                                   # атрибут класса _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):       # дочерний класс Duckbill(PoisonousAnimal, Bird, AquaticAnimal)
    sound = "Click-click-click"                             # звук, издаваемый экземпляром класса

db = Duckbill(10)

print(db.live)

print(db.beak)

db.speak()

db.attack()

db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()



db.lay_eggs()



#Вывод на консоль:

#True

#True

#Click-click-click

#Be careful, i'm attacking you 0_0

#X: 10 Y: 20 Z: 30

#X: 10 Y: 20 Z: 0

#Here are(is) 3 eggs for you # Число может быть другим (1-4)



#По итогу мы должны получить живого утконоса с клювом, атакующего и издающего странные звуки.

#После чего утконос совершает манёвры и ныряет.

#Теперь утконос в безопасности, он откладывает яйца для будущего потомства.



#Примечания:

#Будьте внимательней, когда вызываете методы классов родителей в классе наследнике при множественном наследовании:
# при обращении через super() методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
#При определении порядка наследования обратите внимание на то, что утконос атакует "Be careful, i'm attacking you 0_0"