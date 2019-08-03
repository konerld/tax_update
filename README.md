# Обновление tax для person

## Требования
- python3
- sqlite3


## Создание тестовой базы для проверки на основе db_scheme.sql

    python3 create_db.py



## Запуск скрипта в ручную
    
    python3 main.py



## Автозапуск
Сделать файл исполняемым:

    chmod +x main.py

Для автозапуска скрипта каждые 5минут нужно добавить в crontab запись
    
    */5 * * * * <path to main.py>