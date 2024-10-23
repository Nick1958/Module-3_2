 ## Домашняя работа по уроку "Способы вызова функции", модуль 3_2


# 1a. 	Проверка на корректность e-mail отправителя и получателя, на содержание "@"

def func_send_email(message, recipient, sender="university.help@gmail.com"):

       if recipient.count('@') and sender.count('@') == 1:
          print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)

       else:
          print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)

func_send_email(message=input("Введите сообщение"), recipient=str(input("Введите адрес")), sender=str(input("Введите адрес")))


# 1b. 	Проверка на корректность e-mail отправителя и получателя, содержание '.com' or '.ru' or '.net'

def func_send_email(message, recipient, sender="university.help@gmail.com"):
    variants = ('.com', '.ru', '.net')
    if recipient.endswith(variants) and sender.endswith(variants):
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)

    else:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)

func_send_email(message=input("Введите сообщение"), recipient=str(input("Введите адрес")),
                 sender=str(input("Введите адрес")))

# 2.	Проверка на отправку самому себе

def func_send_email(message, recipient, *, sender="university.help@gmail.com"):
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)

func_send_email(message=input("Введите сообщение"), recipient=str(input("Введите адрес")), sender=str(input("Введите адрес")))


# 3.	Проверка на отправителя по умолчанию.

def func_send_email(message, recipient, *, sender="university.help@gmail.com"):
    print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
func_send_email(message=input("Введите сообщение"), recipient = str(input("Введите адрес")))
