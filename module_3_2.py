# Функция Проверка правильности адресов email
def is_valid(address):  # Проверка правильности адресов email: наличие и окончания адресов на .com, .ru, .net
    if "@" not in address or (".com" not in address and ".ru" not in address and ".net" not in address):
        return False
    return True

# Функция send_email принимает 2 обычных аргумента: сообщение и получатель и 1 именованный аргумент со значением по умолчанию - отправитель.

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if not is_valid(recipient) or not is_valid(sender): #Проверка на корректность e-mail отправителя и получателя.
        print("Invalid address: Невозможно отправить письмо с адреса ", sender, " на адрес ", recipient, ".")
        return
    if sender == recipient: #Проверка на отправку самому себе.
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com": #Проверка на отправителя по умолчанию.
        print("Письмо успешно отправлено с адреса ", sender, " на адрес ", recipient, ".")
        return
    print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, " на адрес ", recipient, ".")
    return

send_email("проба", 'imia.gmail.com', sender = "university.help@gmail.com")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', sender = "university.help@gmail.com")

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')