# Articles CRUD API

REST API для управления статьями, реализованный на Flask.

## Структура проекта

```
/workspace/
├── app/
│   ├── __init__.py      # Основной модуль приложения (Factory pattern)
│   ├── models.py        # Модель данных Article
│   └── controllers.py   # Controller с CRUD операциями
├── run.py               # Точка входа для запуска сервера
├── requirements.txt     # Зависимости
└── README_API.md        # Документация
```

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск сервера

```bash
python run.py
```

Сервер запустится на `http://localhost:5001`

## API Endpoints

### 1. Получить все статьи
**GET** `/api/articles`

Ответ:
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "Заголовок статьи",
      "content": "Текст статьи",
      "author": "Автор",
      "created_at": "2024-01-01T12:00:00",
      "updated_at": "2024-01-01T12:00:00"
    }
  ]
}
```

### 2. Получить статью по ID
**GET** `/api/articles/<id>`

Ответ:
```json
{
  "success": true,
  "data": {
    "id": 1,
    "title": "Заголовок статьи",
    "content": "Текст статьи",
    "author": "Автор",
    "created_at": "2024-01-01T12:00:00",
    "updated_at": "2024-01-01T12:00:00"
  }
}
```

### 3. Создать статью
**POST** `/api/articles`

Тело запроса (JSON):
```json
{
  "title": "Заголовок статьи",
  "content": "Текст статьи",
  "author": "Имя автора"
}
```

Поля:
- `title` (обязательное) - заголовок статьи
- `content` (обязательное) - содержимое статьи
- `author` (необязательное) - автор, по умолчанию "Anonymous"

Ответ:
```json
{
  "success": true,
  "message": "Article created successfully",
  "data": { ... }
}
```

### 4. Обновить статью
**PUT** `/api/articles/<id>`

Тело запроса (JSON) - передаются только поля для обновления:
```json
{
  "title": "Новый заголовок",
  "content": "Обновленный текст"
}
```

Ответ:
```json
{
  "success": true,
  "message": "Article updated successfully",
  "data": { ... }
}
```

### 5. Удалить статью
**DELETE** `/api/articles/<id>`

Ответ:
```json
{
  "success": true,
  "message": "Article deleted successfully"
}
```

## Примеры использования с curl

### Создать статью
```bash
curl -X POST http://localhost:5001/api/articles \
  -H "Content-Type: application/json" \
  -d '{"title":"Моя статья","content":"Содержимое статьи","author":"Иван"}'
```

### Получить все статьи
```bash
curl http://localhost:5001/api/articles
```

### Получить статью по ID
```bash
curl http://localhost:5001/api/articles/1
```

### Обновить статью
```bash
curl -X PUT http://localhost:5001/api/articles/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Обновленный заголовок"}'
```

### Удалить статью
```bash
curl -X DELETE http://localhost:5001/api/articles/1
```

## Технологии

- **Flask** - веб-фреймворк
- **Flask-SQLAlchemy** - ORM для работы с базой данных
- **SQLite** - база данных (хранится в `instance/articles.db`)

## Архитектура

Приложение использует паттерн **Model-View-Controller (MVC)**:

- **Model** (`models.py`) - модель данных Article с методами сериализации
- **Controller** (`controllers.py`) - обработчики HTTP запросов (CRUD операции)
- **App Factory** (`__init__.py`) - функция создания и настройки приложения
