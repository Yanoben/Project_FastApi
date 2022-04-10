# Project_FastApi
АПИ для склада

### Запуск проекта в dev-режиме
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

### GET

`GET /users/`

    curl -i -H 'Accept: application/json' http://0.0.0.0:8000/users/

### Response
    [
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
    ]

### GET ID

`GET /reviews/<
