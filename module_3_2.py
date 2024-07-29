def send_email(message, recipient, *, sender="university.help@gmail.com"):
    no_mail = [".com", ".ru", ".net"]
    dog_symbol = "@"

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    def is_valid_email(email):
        has_at = dog_symbol in email
        has_valid_domain = False
        for domain in no_mail:
            if email[-len(domain):] == domain:
                has_valid_domain = True
                break
        return has_at and has_valid_domain

    valid_recipient = is_valid_email(recipient)
    valid_sender = is_valid_email(sender)

    if valid_recipient and valid_sender:
        if sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')







