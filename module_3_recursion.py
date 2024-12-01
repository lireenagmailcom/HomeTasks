# Задача "Рекурсивное умножение цифр":

# Функция get_multiplied_digits принимает аргумент целое число number и подсчитывает произведение цифр этого числа.

def get_multiplied_digits(number): # c параметром number
    str_number = str(number) # переменная str_number это строковое представление числа number
    if len(str_number) == 1: # если число number < 10, то...
        return number        # ...функция возвращает число number
    first = str_number[0]    # иначе переменной first присваивается первый символ из str_number в числовом представлении(int) и ...
    return int(first) * get_multiplied_digits(int(str_number[1:]))  # ...функция возвращает произведение первой цифры ...
                                                                    # ... числа на значение ф-ции от числа без первой цифры

number = int(input("Введите число: ",)) #  ввод числа
print(get_multiplied_digits(number))    #  вывод произведения цифр этого числа без учета нулей, т.к. при преобразовании ...
                                        # ...строки(str) в число(int) первые нули убираются. Пример, int('00123') -> 123.

