import random
n = random.randint(3, 20)   # генерация случайного числа в диапазоне от 3 до 20
print(n) # вывод сгенерированного числа
string = "" # пустая строка
i = 1
while i >= 1 and i < n/2.0:
    j = i + 1
    while j >= i + 1 and j <= n - i:
        if n % (i + j) == 0:
            string = string + str(i) + str(j)  # к строке дописываем пару, сумма которой i + j является делителем числа n
        j = j + 1
    i = i + 1
print(string) # вывод строки