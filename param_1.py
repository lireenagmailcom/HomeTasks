#Задача "Распаковка":

# 1.Функция с параметрами по умолчанию:

# функция print_params(a = 1, b = 'строка', c = True) принимает 3 параметра со значениями по умолчанию (например: 1, 'строка', True).
# Функция должна выводить эти параметры.
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    return
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params()

# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = 25)

print_params(c=[1, 2, 3])


# 2.Распаковка параметров:

# Создайте список values_list с тремя элементами разных типов.
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).

values_list = [2, 'строка2', False]
print_params(*values_list)

# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).

values_dict = {'a': 'a1', 'b': True, 'c': 100}
print_params(**values_dict)


# 3.Распаковка + отдельные параметры:

# Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = [False, 'список']
# Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)

# Важно!

# Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!

# В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.

# def a(my_list = [])) – это приводит к ошибкам!



# Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)

def append_to_list(item, list_my=None):

    if list_my is None:
        list_my = []
        list_my.append(item)
        print(list_my)
        return

append_to_list("abc")
append_to_list("def")

