# Project_FastApi
АПИ для склада

### Запуск и настройка проекта
- Сначала клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Yanoben/Project_FastApi
```

- Установите и активируйте виртуальное окружение
```
python -m venv venv

. venv/bin/activate
```

- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 

- Потом docker compose, он запускает контейнер БД на postgres:
```
docker-compose -f docker-compose.yaml up
```

- Тепер можно запустить сам проект
```
python main.py
```

## Примеры запроса

### Получение Токена

`GET /users/`

    curl -i -H 'Accept: application/json' http://0.0.0.0:8000/auth/

### Response

    {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.    eyJzdWIiOiJqb2huZG9lQGV4YW1wbGUuY29tIiwiZXhwIjoxNjQ5NjIyMzg2fQ.qNBKd5EFtlmwuK_WYiPiUJNq60EMXm0l2Fqv8B5YVTU",
    "token_type": "Bearer"
    }


### GET

`GET /users/`

    curl -i -H 'Accept: application/json' http://0.0.0.0:8000/users/

### Response
    {
        "id": "1",
        "name": "naem",
        "email": "email@example.com",
        "role": "salesman"
    },
    {
        "id": "2",
        "name": "name",
        "email": "email@example.com",
        "role": "buyer"
    }


### GET

`GET /apples/`

    curl -i -H 'Accept: application/json' http://0.0.0.0:8000/apples/

### Response
    {
        "id": "1",
        "name": "name",
        "description": "text"
    },
    {
        "id": "2",
        "name": "name",
        "description": "text"
    }

