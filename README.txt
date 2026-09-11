Инструкция по запуску проекта "Личный сайт об увлечениях и играх"
Автор: Луцай Иван Григорьевич

1. Откройте папку проекта в Visual Studio Code.
2. Откройте терминал (Ctrl + `).
3. Создайте и активируйте виртуальное окружение:
   python -m venv venv
   # На Windows:
   venv\Scripts\activate
   # На macOS/Linux:
   source venv/bin/activate

4. Установите зависимости:
   pip install -r requirements.txt

5. Примените миграции для базы данных:
   python manage.py makemigrations
   python manage.py migrate

6. Создайте учетную запись администратора (чтобы заходить в /admin):
   python manage.py createsuperuser

7. Запустите сервер:
   python manage.py runserver

8. Откройте в браузере: http://127.0.0.1:8000/
