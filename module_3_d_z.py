def calculate_structure_sum(data):  # определение нашей ф-ции Сумма Структуры Данных с параметром data

    if isinstance(data, int): return data  # если параметр число, то возвращается значение числа

    if isinstance(data, str): return len(data)  # если параметр строка, то возвращается длина строки

    if isinstance(data, list) or isinstance(data, tuple):  # если параметр список/кортеж, то
        ret = 0  # счетчик обнуляется
        for i in range(len(data)):  # цикл по элементам списка/кортежа
            ret += calculate_structure_sum(data[i])  # счетчик += значение нашей ф-ции от i-ого элемента списка/кортежа
        return ret  # возвращается счетчик

    if isinstance(data, set): return calculate_structure_sum(list(data))  # если параметр множество, то возвращается
                    # значение нашей ф-ции от списка элементов множества

    if isinstance(data, dict):  # если параметр словарь, то возвращается
        return calculate_structure_sum(list(data.keys())) + calculate_structure_sum(list(data.values()))
                    # значение нашей ф - ции от списка ключей словаря плюс значение нашей ф-ции от списка значений словаря


data_structure = [  # присвоение значения параметру

    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])

]

result = calculate_structure_sum(data_structure)  # вызов функции с параметром data_structure

print(result)  # вывод значения функции Сумма Структуры Данных на консоль

