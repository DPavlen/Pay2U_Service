# Проект "Pay2U_Service" - направлен на улучшение понимания пользователем сервиса и повышение конверсии. Конечными пользователями являются розничные клиенты банков – пользователи банковских мобильных приложений.

## 1. [Описание](#1)
## 2. [API, эндпойнты для интеграции с фронтендом и другие технические моменты](#2)
## 3. [Запуск проекта в Docker контейнерах с помощью Docker Compose](#3)
## 4. [Ссылка на развернутый проект](#4) 
## 5. [Автор проекта:](#5)

## 1. Описание  <a id=1></a>

Цель проекта Pay2U_Service
Доработать веб-версию сервиса:
- разработать информационную страницу-знакомство о сервисе, его преимуществах и
возможностях при первом входе на сервис;
- добавить интерактивный гайд для объяснения работы с сервисом при первом входе на
сервис;
- оптимизировать главный экран сервиса, изменить представление подписок в каталоге,
добавить популярные товары на главный экран;
- улучшить варианты поиска подписок через разные экраны, добавить возможность
сортировок, ввод параметров и поиска подписок вручную;
- изменить форму представление тарифов подписок через выделение популярных и самых
выгодных тарифов, добавить возможность быстрого ознакомления с тарифами и
сравнения тарифов между собой;
- добавить оповещение пользователям о ценах на подписки;


## 2. API, эндпойнты для интеграции с фронтендом и другие технические моменты <a id=2></a>
- http://127.0.0.1:8000/api/auth/token/login/ Получение токена доступа для аутентификации пользователей в API.
- http://127.0.0.1:8000/api/auth/token/logout/ Удаление токена доступа для завершения сеанса аутентифицированного пользователя в API.
- http://127.0.0.1:8000/api/v1/users/,  Работа с пользователями. Регистрация пользователей.
Вывод пользователей. У авторизованных пользователей. POST и GET запросы.
- http://127.0.0.1:8000/api/v1/users/me/ GET-запрос просмотр информации о себе(авторизован). PATCH-запрос возможность изменять поля: Имя, Фамилия, Индикатор первого входа.
- http://127.0.0.1:8000/api/v1/categories/ Запрос для получения всех категорий, GET запрос.  
- http://127.0.0.1:8000/api/v1/categories/{id} Подробная информация о выбранной категории. С возможность CRUD.
- http://127.0.0.1:8000/api/v1/services/ Просмотр списка сервисов. GET запрос.
- http://127.0.0.1:8000/api/v1/services/{id} Подробная информация о выбранной сервисе. С возможность CRUD.
- http://127.0.0.1:8000/api/v1/categories/{id}/services Вывод всех сервисов к определенному id сервиса. GET запрос.
- http://127.0.0.1:8000/api/v1/services/{id}/add/ Добавить новую подписку пользователю на определенный сервис.
- http://127.0.0.1:8000/api/v1/services/{id}/tariff/ Получить все тарифы к определенному id сервиса. GET запрос.
- http://127.0.0.1:8000/api/v1/services/{id}/popular/ Получить все популярные сервисы. GET запрос.
- http://127.0.0.1:8000/api/v1/subscriptions/ Список всех подписок пользователя. С возможность CRUD.
- http://127.0.0.1:8000/api/v1/payment_methods/ Получить все методы оплат. GET запрос(только авторизованного пользователя)
- http://127.0.0.1:8000/api/v1/payment_methods/{id}/subscription_payments/ Получить по способам оплат текущего userа его оплаты/подписки. GET запрос.
- http://127.0.0.1:8000/api/v1/service_cashback/  Просмотр всех кэшбэков сервиса
- http://127.0.0.1:8000/api/v1/user_cashback/  Просмотр кэшбэка определенного сервиса

## 3. Стек технологий проекта <a id=3></a>
[![Django](https://img.shields.io/badge/Django-4.2.1-6495ED)](https://www.djangoproject.com) [![Djangorestframework](https://img.shields.io/badge/djangorestframework-3.14.0-6495ED)](https://www.django-rest-framework.org/) [![Django Authentication with Djoser](https://img.shields.io/badge/Django_Authentication_with_Djoser-2.2.0-6495ED)](https://djoser.readthedocs.io/en/latest/getting_started.html) [![Nginx](https://img.shields.io/badge/Nginx-1.21.3-green)](https://nginx.org/ru/) [![React](https://img.shields.io/badge/React-18.2.0-blue)](https://react.dev/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)](https://www.postgresql.org/) [![YandexCloud](https://img.shields.io/badge/yandex-cloud-5282FF?logo=yandexcloud)](https://www.cloud.yandex.com/)

- Веб-сервер: nginx (контейнер nginx)  
- Frontend фреймворк: React.js (контейнер frontend)  
- Backend фреймворк: Django (контейнер backend)  
- API фреймворк: Django REST (контейнер backend)  
- База данных: PostgreSQL (контейнер db)

Веб-сервер nginx перенаправляет запросы клиентов к контейнерам frontend и backend, либо к хранилищам (volume) статики и файлов.  
Контейнер nginx взаимодействует с контейнером backend через gunicorn.  
Контейнер frontend взаимодействует с контейнером backend посредством API-запросов и передачи информации на фронтенд.


## 3. Запуск проекта в Docker контейнерах с помощью Docker Compose <a id=3></a>

Склонируйте проект из репозитория:
```bash
git clone https://github.com/DPavlen/Pay2U_Service.git
```
Перейдите в директорию проекта Hackathon_team_8:
```bash
cd Pay2U_Service/
```
Создайте файл .env для PostgreSQL в корне проекта и контейнера backend, впишите в него переменные для инициализации БД и связи с ней. Затем добавьте строки, содержащиеся в файле .env.example и подставьте свои значения.
Пример из файла с расширением .env:
```bash
# Мы используем СУБД PostgreSQL, необходимо заполнить следующие константы.
POSTGRES_USER=your_django_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=db_name
# Добавляем переменные для Django-проекта:
DB_HOST=db
DB_PORT=port_for_db  # Default is 5432
# Настройки настройки переменных settings
SECRET_KEY=DJANGO_SECRET_KEY  # Your django secret key 'django-insecure......'
DEBUG=True # Set to True if you do need Debug.
ALLOWED_HOSTS=127.0.0.1 # localhost by default if DEBUG=False
```
Запустите Docker Compose с этой конфигурацией на своём компьютере. Название файла конфигурации надо указать явным образом, ведь оно отличается от дефолтного. Имя файла указывается после ключа -f:
```bash
docker compose -f docker-compose.production.yml up
```
Команда описанная выше, сбилдит Docker образы и запустит backend, frontend, СУБД и Nginx в отдельных Docker контей.
Выполните миграции в контейнере с backend и необходимо собрать статику backend'a, поочередно выполните 2 команды:
```bash
sudo docker compose -f docker-compose.yml exec careerhub-backend python manage.py makemigrations
sudo docker compose -f docker-compose.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.yml exec backend python manage.py collectstatic
```
Создать суперюзера (Администратора):
```bash
sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
```

Переместите собранную статику в volume(Данные можно сохранить отдельно от контейнера: для этого придумали Docker volume), 
созданный Docker Compose для хранения статики:
```bash
sudo docker compose -f docker-compose.yml exec backend cp -r /app/collected_static/. /static/static/
```
По завершении всех операции проект будет запущен и доступен по адресу:
```bash
http://127.0.0.1/
```
Останавливает все сервисы, связанные с определённой конфигурацией Docker Compose. 
Для остановки Docker контейнеров выполните следующую команду в корне проекта:
```bash
sudo docker compose -f docker-compose.yml down
```

## 4. Ссылка на развернутый проектe <a id=4></a>
Ссылка на развернутый проект будет чуть позже https://


## 5. Автор проекта: <a id=5></a> 

**Павленко Дмитрий**  
- Ссылка на мой профиль в GitHub [Dmitry Pavlenko](https://github.com/DPavlen)  

**Бобков Константин**  
- Ссылка на мой профиль в GitHub [German Leontiev](https://github.com/Leontiev93)