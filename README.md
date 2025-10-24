# Финальный проект — вторая часть (Яндекс.Самокат)

**Автор:** Йийит Валентина  
**Когорта:** 36  
**Проект:** Финальный проект, вторая часть

## Состав репозитория
- `queries.sql` — SQL для двух заданий по БД
- `configuration.py` — базовый URL и пути API
- `data.py` — тело заказа для создания
- `sender_stand_requests.py` — функции запросов (создание заказа / получение по треку)
- `tests/test_order_api.py` — автотест: создать заказ → получить по треку → код ответа 200
- `artifacts/screenshot_test_result.png` — сюда положите скрин запуска теста в VS Code
- `.gitignore`, `requirements.txt`

## Как запустить тест
```bash
python -m venv venv
# Windows PowerShell:
Set-ExecutionPolicy RemoteSigned -Scope Process
.venv\Scripts\Activate
pip install -r requirements.txt
pytest -v
```
## Где логи
Логи сервера находятся в файле:
/var/www/backend/logs/error.log

