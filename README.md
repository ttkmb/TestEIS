# Проект по расчету квартплаты

Этот проект реализует систему управления данными по домам, квартирам, счетчикам воды и тарифам, а также расчета квартплаты для всех квартир в доме. Проект включает API для ввода и вывода данных, а также фоновый процесс расчета квартплаты с использованием Celery.

## Стек технологий

- Django
- Celery
- Redis
- PostgreSQL

## Установка и запуск

Зависимости: pip install -r requirements.txt

### Не забудьте создать файл .env - пример .env.sample

## Настройка базы данных
python manage.py migrate

## Запуск Celery

celery -A ваш_проект worker --loglevel=info

# API Эндпоинты
- GET /api/houses/ - Получение списка данных по домам
- GET /api/houses/{id}/ - Получение данных по конкретному дому
- POST /api/houses/{id}/calculate_billing/ 
{
  "year": 2024,
  "month": 6
} - Расчет квартплаты по дому 
- GET /api/houses/{id}/get_billing/?year=2024&month=6 - Получение данных по квартплате за месяц

## Для удобного тестирования и документирования API используйте Swagger. После запуска сервера перейдите по адресу /api/swagger/
