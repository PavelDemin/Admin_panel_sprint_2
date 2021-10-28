## Установка

1. Склонировать проект командой `git clone https://github.com/PavelDemin/Admin_panel_sprint_2.git`
2. В корне проекта создать конфигурационный файл `.env` со следующим содержимым:
   1. `SECRET_KEY="указать секретный ключ"`
   2. `DEBUG=1` - 1 - включен debug, 0 - выключен debug
   3. `POSTGRES_DB="movies"` - имя базы данных
   4. `POSTGRES_PASSWORD="qwerty123"` - пароль к базе данных
   5. `POSTGRES_HOST="postgres"` - хост базы данных
   6. `POSTGRES_PORT=5432` - стандартный порт
   7. `POSTGRES_USER="postgres"` - имя пользователя базы данных
3. Запустить контенеры командой `docker-compose up -d`
4. Для миграций запустить команду `docker exec django-app python manage.py migrate`
5. Для сборки статических файлов запустить команду `docker exec django-app python manage.py collectstatic`
6. Для создания учетной записи администратора запустить команду `docker exec -ti django-app python manage.py createsuperuser`
7. Приложение запущено [http://localhost](http://localhost)




