# Задача "Нули ничто, отрицание недопустимо!":
# Выводить на консоль элементы списка кроме равных 0 до первого отрицательного элемента
# Напишите цикл while с соответствующими задаче условиями.
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i <= len(my_list) and my_list[i] >= 0:    # Пока индекс не превышает длины списка и текущий элемент неотрицателен
    if my_list[i] > 0:                          # только положительные элементы списка выводятся на консоль
        print(my_list[i])                       # вывод на консоль очередного элемента списка
    i = i + 1                                   # переход к следующему индексу всегда