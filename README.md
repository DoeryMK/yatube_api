# yatube_api

## Социальная сеть блогеров API

## **Краткое описание**
Данный проект является учебным. 
Основная цель проекта - получение навыков работы создания REST API.

### _Доступные возможности_

* Получение, проверка и обновление токена-аутентификации
* Добавление, корректировка и удаление публикации
* Добавление, корректировка и удаление комментария к публикации
* Просмотр публикаций и комментариев к ним
* Просмотре сообществ и информации о них
* Подписка на пользователя и просмотр подписчиков

* Реализовано разграничение прав пользователей посредством собственного класса, на уровне проекта - доступ для всех
* На уровне проекта установлено ограничение на количество разрешенных запросов к API
* Настроена пагинация

## **Требования**

Django==2.2.16  
python-dotenv==0.19.0  
djangorestframework==3.12.4  
djangorestframework-simplejwt==4.7.2  
djoser==2.1.0  
Pillow==8.3.1  
PyJWT==2.1.0  
requests==2.26.0  

## **Запуск проекта**

В консоли выполните следующие команды:

1. Клонировать проект из репозитория
```
git clone git@github.com:DoeryMK/yatube_api.git
```
или
```
git clone https://github.com/DoeryMK/yatube_api.git
```
2. Перейти в папку с проектом и создать виртуальное окружение
```
cd <имя папки>
```
```
python -m venv venv
```
или
```
python3 -m venv venv
```
3. Активировать виртуальное окружение
```
source venv/Scripts/activate
```
или
```
source venv/bin/activate
```
4. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
5. Перейти в папку yatube и выполнить миграции
```
cd yatube
```
```
python manage.py makemigrations
```
или 
```
python3 manage.py makemigrations
```
```
python manage.py migrate
```
или
```
python3 manage.py migrate
```
6. Перейти в папку yatube/yatube и создать файл .env. В файле указать значение SECRET_KEY. 
```
SECRET_KEY = *ваш уникальный секретный ключ Django*
```
7. Запустить проект
```
python manage.py runserver
```
или 
```
python3 manage.py runserver
```

## **Тестирование через HHTP-клиент**
Для тестирования работы API проекта можно воспользоваться HHTP-клиентом [Postman](https://www.postman.com) или [httpie](https://httpie.io). 
## **Пример запросов и ответов**

_Redoc доступен по ссылке_ http://127.0.0.1:8000/redoc/


1. *Получение публикаций* 
При указании параметров limit и offset выдача должна работать с пагинацией.

GET-запрос к эндпоинту http://127.0.0.1:8000/api/v1/posts/
Request
```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
    {}
    ]
}
```
2. *Обновление публикации* 
Обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
PUT-запрос к эндпоинту http://127.0.0.1:8000/api/v1/posts/{id}/
Request
```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
Response
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
3. *Добавление комментария*
POST-запрос к эндпоинту http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
Request
```
{
    "text": "string"
}
```
Response
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```
4. *Подписки*
Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.
Возможен поиск по подпискам по параметру search
GET-запрос к эндпоинту http://127.0.0.1:8000/api/v1/follow/

Request
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```
4. *Получение JWT-токен*
POST-запрос к эндпоинту http://127.0.0.1:8000/api/v1/jwt/create/

Request
```
{
  "username": "string",
  "password": "string"
}
```
Response
```
{
"refresh": "string",
"access": "string"
}
```

### Авторы

DoeryMK