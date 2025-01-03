#Задание "Свой YouTube":
import time                                             # import модуля time

class User:                                             # создание нового класса User

    def __init__(self,  nickname, password, age):       # определение метода __init__ в классе User
        self.nickname = nickname                        # c атрибутами объекта self.nickname, self.password, self.age
        self.password = hash(password)
        self.age = age

    def __contains__(self, item):                       # определение ф-ции _contains__ с параметром item
        return self.nickname == item                    # возвращает True, если self.nickname == item

    def __repr__(self):                                 # определение  ф-ции __repr__(self)
        return self.nickname                            # возвращает строку self.nickname

    def __eq__(self, other):                            # определение  ф-ции __eq__(self, other)
        if not isinstance(other, User): return False    # возвращает False, если other не является объектом класса User
        return self.nickname == other.nickname          # иначе возвращает True, если self.nickname == other.nickname


class Video:                                            # создание нового класса Video

    def __init__(self, title, duration, adult_mode = False):  # определение метода __init__ в классе Video
        self.title = title                              # c атрибутами объекта self.title, self.duration, self.adult_mode
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __contains__(self, item):                       # определение ф-ции _contains__ с параметром item
        return self.title == item                       # возвращает True, если self.title == item

    def __repr__(self):                                 # определение  ф-ции __repr__(self)
        return self.title                               # возвращает строку self.title

    def __eq__(self, other):                            # определение  ф-ции __eq__(self, other)
        if not isinstance(other, Video): return False   # возвращает False, если other не является объектом класса Video
        return self.title == other.title                # иначе возвращает True, если self.title == other.title


class UrTube:                                           # создание нового класса UrTube

    def __init__(self):                                 # определение метода __init__ в классе UrTube
        self.users = []                                 # пустой список пользователей
        self.videos = []                                # пустой список видео
        self.current_user = None                        # текущий пользователь - объект типа None

    def __find_user(self, nickname):                    # определение  ф-ции __find_user с параметром nickname
        user = User(nickname, "", 0)      # создается объект класса User с параметрами nickname, "", 0
        ind = self.users.index(user) if user in self.users else -1  # переменной ind присваивается значение индекса
                                                        # созданного объекта user в списке users, если он там есть, иначе -1
        return self.users[ind] if ind >= 0 else None    # возвращает элемент списка с индексом ind, если ind>=0 иначе None

    def __find_video(self, title):                      # определение  ф-ции __find_video с параметром title
        video = Video(title, 0)                 # создается объект класса Video с параметрами title, 0
        ind = self.videos.index(video) if video in self.videos else -1  # переменной ind присваивается значение индекса
                                                        # созданного объекта video в списке videos, если он там есть, иначе -1
        return self.videos[ind] if ind >= 0 else None   # возвращает элемент списка с индексом ind, если ind>=0 иначе None

    def log_in(self, nickname, password):               # определение метода log_in c параметрами nickname, password
        user = self.__find_user(nickname)               # переменной user задается значение ф-ции __find_user(nickname)
        if user != None and user.password == hash(password):  # если user != None и пароли совпадают, то
            self.current_user = user                    # переменной current_user присваивается значение user

    def register(self, nickname, password, age):        # определение метода register с параметрами: nickname, password,age
        user = self.__find_user(nickname)               # переменной user задается значение ф-ции __find_user(nickname)
        if user != None:                                # если user существует, то вывод информации об этом м выход,
            print(f"Пользователь {nickname} уже существует")
            return                                      # иначе переменной current_user присваивается значение вновь
        self.current_user = User(nickname, password, age)  # созданного объекта User с атрибутами nickname, password, age
        self.users.append(self.current_user)            # и переменная current_user дописывается в конец списка users

    def log_out(self):                                  # определение метода log_out
        self.current_user = None                        # текущий пользователь сбрасывается, ему присваивается значение None.

    def add(self, *args):                               # определение метода add, который принимает неограниченное кол-во
        for i in range(len(args)):                      # параметров и перебирает их в цикле, если параметр из класса Video
            if isinstance(args[i], Video) and args[i] not in self.videos:   # и если такого видео ещё нет в списке videos
                self.videos.append(args[i])             # то добавляет его в список videos

    def get_videos(self, search):                       # определение метода get_videos, который принимает поисковое слово
        ret = []
        for i in range(len(self.videos)):               # и в цикле до конца списка videos проверяет условие вхождения:
            if search.lower() in self.videos[i].title.lower():  # если поисковое слово входит в название видео из списка
                ret.append(self.videos[i])              # videos, то дописывает видео в список найденных видео и
        return ret                                      # возвращает список всех найденных видео

    def watch_video(self, title):                       # определение метода watch_video, который принимает title видео
        video = self.__find_video(title)                # и ищет полное совпадение
        if video != None:                               # если видео существует,
            if self.current_user == None:               # то если current_user не определен,
                print("Войдите в аккаунт, чтобы смотреть видео") # печать сообщения о необходимости войти в аккаунт
                return                                  #  для просмотра и выход
            if video.adult_mode and self.current_user.age < 18: # если есть ограничения по возрасту и возраст юзера<18,
                print("Вам нет 18 лет, пожалуйста покиньте страницу") # то печать сообщения о необходимости покинуть сайт
                return                                  # и выход
            j = video.time_now                          # j - счетчик секунд, устанавливается на время просмотра = 0
            while j < video.duration:                   # пока j<продолжительности видео:
                time.sleep(1)                           # пауза длительностью 1 секунда
                j += 1                                  # увеличение счетчика на 1 секунду
                video.time_now = j                      # установка времени просмотра на новое значение счетчика
                print(j, end = ' ')                     # печать счетчика без перевода строки
            print("Конец видео")                        # после выхода из цикла печать информации о завершении просмотра


ur = UrTube()                                                                           # создание объекта UrTube
v1 = Video('Лучший язык программирования 2024 года', 200)                  # создание объекта Video
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)   # создание объекта Video
ur.add(v1, v2)                                                                    # добавление видео
print(ur.get_videos('лучший'))                                                          # проверка поиска 'лучший'
print(ur.get_videos('ПРОГ'))                                                            # проверка поиска 'ПРОГ'
ur.watch_video('Для чего девушкам парень программист?')                            # проверка на вход пользователя
ur.register('vasya_pupkin', 'lolkekcheburek', 13)           # регистрация пользователя <18
ur.watch_video('Для чего девушкам парень программист?')                            # проверка на возрастное ограничение
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  # регистрация пользователя >18
ur.watch_video('Для чего девушкам парень программист?')                            # просмотр
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)      # попытка повторной регистрации
print(ur.current_user)                                                         # печать инфо о текущем пользователе
ur.watch_video('Лучший язык программирования 2024 года!')                      # попытка просмотра несуществующего видео