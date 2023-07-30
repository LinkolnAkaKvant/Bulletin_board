# Bulletin_board

---

## Description

Django applications for creating and viewing ads. | Приложения Django для создания и просмотра рекламы.

___

## Особенности проекта | Project Features

- Проект имеет регистрацию пользователя, восстановление пароля через email.
- В проекте мы можем создавать, редактировать, удалять, изменять объявления, другие пользователи могут их комментировать.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

___

## Stack:
Python 3.10

Django 4.1.7

PostgresQL

Docker

---

## Запуск проекта | Launch of the project ##

### 1 ###

#### Создание виртуального окружения | Creating a Virtual Environment: ####

- python -m venv venv

### 2 ###

#### Установка зависимостей | Setting dependencies: ###

 - pip install -r requirements.txt

### 3 ###

#### Скрытые переменные должны хранится в файле | Hidden variables must be stored in the file: ####

- .env

### 4 ###

#### Создание и применение миграций | Creating and implementing migration: ####

- python manage.py makemigrations 

- python manage.py migrate

### 5 ###

#### Создание и запуск контейнеров в Docker | Create and run containers in Docker: ####


- docker-compose up --build -d

### 6 ###

#### Команда для запуска проекта | Project start command: ####

- python manage.py runserver