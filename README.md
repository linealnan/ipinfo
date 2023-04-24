Сервис получения информации об ip адресе
========================

Запуск дев окружения
-------------------------

- запустить venv:
```bash
python3 -m venv virtual/environment/
```

- Запустите необходимые сервисы:
```bash
docker-compose -f docker/docker-compose.dev.yml up -d
```

- запустить сервинг следцующей командой:
```bash
    uvicorn main:app --reload
```
