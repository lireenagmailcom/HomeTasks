def divide(first, second):
    if second == 0:
        from math import inf
        a = inf
        return a
    a = first/second
    return a

#first = int(input('Введите делимое: '))
#second = int(input('Введите делитель: '))
#print(divide(first, second))