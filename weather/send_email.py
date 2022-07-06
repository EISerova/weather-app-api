from django.core.mail import send_mail

SINGUP_MESSAGE = "Вы зарегистрировались на сервисе погоды. Ваш логин: {username}."


def send_weather_mail(
    message,
    recipient_list,
    subject="Прогноз погоды",
    from_email="katyaserova@yandex.ru",
):
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )


def send_singup_mail(
    username,
    email,
    subject="Информация о регистрации",
    from_email="katyaserova@yandex.ru",
):
    message = SINGUP_MESSAGE.format(username=username)
    send_mail(
        subject,
        message,
        from_email,
        recipient_list=[email],
        fail_silently=False,
    )
