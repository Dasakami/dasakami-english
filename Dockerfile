# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем все файлы проекта в контейнер
COPY . /app/

# Устанавливаем зависимости из requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Открываем порт, на котором будет работать сервер
EXPOSE 8000

# Команда для запуска Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
