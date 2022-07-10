from django.core.mail import send_mail

from weather_app.settings import EMAIL_HOST_USER

SINGUP_MESSAGE = "Вы зарегистрировались на сервисе погоды. Ваш код подтверждения: {confirmation_code}."
TOKEN_MESSAGE = "Ваш токен для доступа на сервис погоды: {token}.  Сохраните его!"


def send_weather_mail(
    message,
    recipient_list,
    subject="Прогноз погоды",
    from_email=EMAIL_HOST_USER,
):
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )


def send_singup_mail(
    email,
    confirmation_code,
    subject="Информация о регистрации",
    from_email=EMAIL_HOST_USER,
):
    message = SINGUP_MESSAGE.format(confirmation_code=confirmation_code)
    send_mail(
        subject,
        message,
        from_email,
        recipient_list=[email],
        fail_silently=False,
    )


def send_token_mail(
    email,
    token,
    subject="Ваш токен для доступа на сервис погоды",
    from_email=EMAIL_HOST_USER,
):
    message = TOKEN_MESSAGE.format(token=token)
    send_mail(
        subject,
        message,
        from_email,
        recipient_list=[email],
        fail_silently=False,
    )
