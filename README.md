### _Спиридонов Роман (Speccy-Rom)_
Мое Резюме: https://hh.ru/resume/4a35d0b9ff0843acf50039ed1f644e61787345

## Тестовое задание

### Задание :white_check_mark:
Разработайте приложение позволяющие получать информацию про погодные условия в различных городах мира.
Используйте: API для погоды: https://openweathermap.org/, Django 3 +, SQlite
Ввод города должен происходить из формы front-end(+ админки) и выводится на экран.


Склонируйте репозиторий с помощью git

   git clone https://github.com/Speccy-Rom/WeatherApp.git
Перейти в папку:
```bash
cd WeatherApp
```
Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```
Перейти в папку с manage.py:
```bash
cd orders
```
# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```
Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:
по умолчанию Имя пользователя admin пароль: 123266
```bash
Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): *****
Superuser created successfully.
```
* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/`
