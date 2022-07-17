# Weather App Api
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)    
![Docker](https://a11ybadges.com/badge?logo=docker) ![PostgreSQL](https://a11ybadges.com/badge?logo=postgresql) ![Celery](https://a11ybadges.com/badge?logo=celery) ![Redis](https://a11ybadges.com/badge?logo=redis)

### Описание:

Информирование о погоде в городе. Для регистрации указывается только почта. После регистрации с выбранной периодичностью на почту приходить информация о погоде: "температура", "ощущается как", "давление". 

## Примеры API-запросов:

#### Регистрация

```http
  GET /api/v1/auth/signup/
```

| Parameter          | Type     | Description                    |
| :----------------- | :------- | :----------------------------- |
| `email`            | `string` | **Required**. Ваша почта       |


#### Получение токена

```http
  GET /api/v1/auth/token/
```

| Parameter          | Type     | Description                     |
| :----------------- | :------- | :------------------------------ |
| `email`            | `string` | **Required**. Ваша почта        |
| `confirmation_code`| `string` | **Required**. Код подтверждения |

#### Подписка на погоду в городе

```http
  GET /api/v1/subscribe/
```

| Parameter          | Type     | Description                    |
| :----------------- | :------- | :----------------------------- |
| `token`            | `string` | **Required**. Ваш токен        |
| `town`             | `string` | **Required**. Название города  |
| `update_period`    | `integer`| **Optional**. Период рассылки  |


### Зависимости:

Django 3.2  
Django rest framework 3.12  
Psycopg2 2.9  
Redis 3.5  
Celery 5.1  

### Запуск проекта в Docker

Клонировать репозиторий

```bash
  git clone git@github.com:EISerova/weather-app-api.git
```

Запустить контейнер
```power shell
  docker-compose up -d --build
```

### В планах:
Добработать редактирование и удаление подписки, написать тесты, сделать фронтенд на javascript.

### Автор: 
Серова Екатерина

### Обратная связь:
Если у вас есть предложения или замечания, пожалуйста, свяжитесь со мной - katyaserova@yandex.ru

### Лицензия:
[MIT](https://choosealicense.com/licenses/mit/)