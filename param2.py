# Задача "Однокоренные":

# Функция single_root_words составляет новый список same_words только из тех слов
# списка other_words, которые содержат root_word или, наоборот, root_word содержит одно из слов этого списка
# Функция single_root_words возвращает список same_words в качестве результата своей работы

def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if other_words[i].upper() in root_word.upper() or root_word.upper() in other_words[i].upper():
            same_words.append(other_words[i])
        i += 1
    return (same_words)

#Вызов функции single_root_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

#Вывод на экран(консоль) возвращённых значений
print(result1)
print(result2)
