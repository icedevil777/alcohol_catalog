# Каталог Алкоголя

## Запустить postgres в докере или иным путем.
```bash
docker-compose up --build
```
## Применить миграции
```bash
python manage.py migrate
```

## Можно загрузить fixture
```bash
python manage.py loaddata data.json
```

## Запустить сервер
```bash
python manage.py runserver
```

![site.png](..%2F..%2F%D0%98%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F%2Fsite.png)