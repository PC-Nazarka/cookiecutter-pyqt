{{cookiecutter.project_name}}

## Установка

1. Установка зависимостей и подключение к окружению
```bash
poetry install
poetry shell
```

2. Запуск приложения
```bash
make run
```

# Конвертирование файла
Перед конвертированием необходимо запустить виртуальное окружение

```bash
make convert
```
{% if cookiecutter.pyinstaller != 'n' %}
# Сборка приложения
Запуск процесса сборки
```bash
make build
```
{% endif -%}