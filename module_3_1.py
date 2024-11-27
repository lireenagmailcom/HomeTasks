
# Задача "Счётчик вызовов":

calls = 0   # глобальная переменная calls = 0

def count_calls():  # Определение функции Счетчик Вызовов
    global calls    # в функуии используется глобальная переменная calls
    calls += 1      # значение переменной calls увеличивается на 1.
    return

def string_info(string):  # Определение функции Информация о строке
    print((len(string), string.upper(), string.lower()))  # вывод на консоль кортежа из длины строки, строки в верх. и нижн. регистрах
    count_calls()  # вызов функции Счетчик Вызовов
    return

def is_contains(string, list_to_search):    # Определение функции is_contains с двумя параметрами string и list_to_search.
    i = 0                                   # функция возвращает True, если строка находится в этом списке, False - если отсутствует.
    while i < len(list_to_search) and string.upper() != list_to_search[i].upper():
        i += 1
    count_calls()  # вызов функции Счетчик Вызовов
    if i == len(list_to_search):
        return False
    return True

string_info('Capibara')
string_info('Armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



# print(string_info('Capybara'))
# print(string_info('Armageddon'))
# print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
# print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
# print(calls)



