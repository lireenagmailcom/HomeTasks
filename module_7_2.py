# Задача "Записать и запомнить":

def custom_write(file_name, strings):           # функция с аргументами file_name и strings (файл и список строк для записи)
    strings_positions = {}                      # создается пустой словарь strings_positions
    fp = open(file_name, 'w', encoding='utf-8') # открывается файл для записи с кодировкой utf-8
    for i in range(len(strings)):               # в цикле по строкам для записи:
        tup = (i+1, fp.tell())                  # создаем ключ - кортеж (номер строки, номер байта, с которого начинается эта строка)
        strings_positions[tup] = strings[i]     # для ключа tup определяется значение словаря = strings[i]
        fp.write(strings[i]+'\n')               # запись строки strings[i] с добавленным разделителем строк'\n'
    fp.close()                                  #  файл закрывается
    return strings_positions                    #  возвращается словарь strings_positions


name = 'test.txt'
info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write(name, info)

for elem in result.items():
    print(elem)