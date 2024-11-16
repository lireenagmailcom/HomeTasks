first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
#print(first, second, third)
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second and first != third and second != third:
    print(0)
else:
    print(first, second, third)
#  В конспекте программа заканчивалась строкой "else:", но у меня требовали продолжения банкета: IndentationError: expected an indented block after 'else' statement on line 11
# пришлось скопировать команду времен отладки. Объясните, пожалуйста, что значит IndentationError: ожидался отступ после оператора «else» в строке 11