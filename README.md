# test_task

![Static Badge](https://img.shields.io/badge/python-3.11-blue?logo=python&link=https%3A%2F%2Fwww.python.org%2F)
![Static Badge](https://img.shields.io/badge/django-4%2C2-%23092E20?logo=django&link=https%3A%2F%2Fwww.djangoproject.com%2F)
![Static Badge](https://img.shields.io/badge/DRF-3%2C14-%23ED1C24?link=https%3A%2F%2Fwww.django-rest-framework.org%2F)


## О проекте

Тестовое задание по созданию API для управления списком задач

- **[Python](https://www.python.org/)** (version 3.11)
- **[Django](https://www.djangoproject.com/)**
- **[DRF](https://www.django-rest-framework.org/)**
- **[PostgreSQL](https://www.postgresql.org/)**
- **[Docker Compose](https://docs.docker.com/compose/)**

## Запуск

Склонируйте проект:

```
git clone https://github.com/Niolum/test_task.git
```

Далее настройте виртуальную среду и основные зависимости из файла ``requirements.txt``

```
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```

Затем создайте файл .env. установить переменные среды и создать базу данных.

Example ``.env``:

```
DBUSER=username
DBPASS=password
DBNAME=db_name
DBHOST=localhost
DBPORT=5432

DEBUG=0
SECRET_KEY='some_secret_key'
DJANGO_ALLOWED_HOSTS="*"
```

Перед запуском нужно выполнить несколько команд:

```
python manage.py migrate
python manage.py collectstatic
```

Запустить приложение:

```
python manage.py runserver
```

И перейти по указанному адресу, чтобы открыть документацию Swagger:

```
http://127.0.0.1:8000/swagger/
```


Для запуска в docker-compose меняем ``.env``:

```
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=db_name

DBUSER=username
DBPASS=password
DBNAME=db_name
DBHOST=postgres
DBPORT=5432

DEBUG=0
SECRET_KEY='some_secret_key'
DJANGO_ALLOWED_HOSTS="*"
```

Перед запуском docker-compose выполняем команды:

```
docker volume create taskdb
docker volume create static_django_task
```

Чтобы запустить проект, используйте следующую команду:

```
docker-compose up -d
```