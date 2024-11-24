# Задача "Всё не так уж просто":

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
primes = []  # список primes содержащий только простые числа.
not_primes = []  # список not_primes, содержащий все составные числа.

for i in range(len(numbers)):                # цикл по списку исследуемых чисел

    if numbers[i] != 1:                      # если иссл. число != 1, то
        is_prime = True                      # установливается флаг "Простое число" и начинается
        for j in range(len(primes)):         # цикл по списку простых чисел
            if numbers[i] % primes[j] == 0:  # если исследуемое число делится на число из списка простых чисел,
                is_prime = False             # то установливается флаг "Составное число" и...
                break                        # ...и цикл по списку простых чисел прерывается
            else:                            # если исследуемое число не делится на число из списка простых чисел и...
                if primes[j] >= int(numbers[i] ** 0.5): # ...и если число из списка простых чисел не меньше квадрат. корня из иссл.числа,
                    break                    # то цикл по списку простых чисел прерывается

        if is_prime:                         # если флаг "Простое число", то
            primes.append(numbers[i])        # исследуемое число добавляется в конец списка простых чисел
        else:                                # если флаг "Составное число", то
            not_primes.append(numbers[i])    # исследуемое число добавляется в конец списка составных чисел

print(primes)                                # список простых чисел выводится на консоль
print(not_primes)                            # список составных чисел выводится на консоль