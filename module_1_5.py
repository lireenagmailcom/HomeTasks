#  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var = (1, 2, 3.0, 4.0, 'неизменяемый кортеж', ['a','b','c'])
#  - Выполните операции вывода кортежа immutable_var на экран.
print ('Immutable tuple:', immutable_var)
# - Попытайтесь изменить элементы кортежа immutable_var.
#immutable_var[3] = 7
#print (immutable_var)
# Если убрать знак комментария в строках 6 и 7, то появляется сообщение:
#                         1 строка:  File "C:\Users\liree\PycharmProjects\BSD\module_1_5.py", line 6
#                         2 строка:    immutable_var[3] = 7
#                         3 строка: IndentationError: unexpected indent
# Т.е., попытка изменить элемент кортежа приводит к ошибке, потому что кортеж - это неизменяемый объект'''

#  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list = [1, 2, 3.0, 4.0, 'список', ['a','b','c']]
  # Измените элементы списка mutable_list.
print('Mutable list:', mutable_list)
mutable_list[4] = 'измененный список'
print('Mutable list:', mutable_list)
  #- Выведите на экран измененный список mutable_list.



#Примечания:

#- Для вывода значений на экран используйте функцию print().

#- Обратите внимание на особенности изменяемых и неизменяемых объектов в Python.