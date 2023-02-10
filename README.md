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

![site.png](media_root%2Fsite.png)