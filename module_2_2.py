first = int(input('Введите первое число: '))    # ввод первого числа
second = int(input('Введите второе число: '))   # ввод второго числа
third = int(input('Введите третье число: '))    # ввод третьего числа

if first == second and first == third:          # если все 3 числа равны между собой
    print(3)                                    # выводится 3
elif first == second or first == third or second == third: # если только любые 2 числа равны между собой
    print(2)                                    # выводится 2
else:                                           # если все 3 числа не равны между собой
    print(0)                                    # выводится 0

