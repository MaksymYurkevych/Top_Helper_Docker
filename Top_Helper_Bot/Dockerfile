# Docker-команда FROM вказує базовий образ контейнера
FROM python:3.10-slim-buster

# Встановимо змінну середовища
# ENV APP_HOME /app

# Встановимо робочу директорію усередині контейнера
WORKDIR .

# COPY poetry.lock $APP_HOME/poetry.lock
# COPY pyproject.toml $APP_HOME/pyproject.toml
# Скопіюємо інші файли до робочої директорії контейнера
COPY . .

# Встановимо залежності усередині контейнера
# RUN pip install poetry
# RUN poetry config virtualenvs.create false && poetry install --only main
RUN pip install -r requirements.txt

# Позначимо порт де працює програма всередині контейнера
EXPOSE 5000

# Запустимо нашу програму всередині контейнера
ENTRYPOINT ["python", "menu.py"]