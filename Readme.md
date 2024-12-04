Название проекта - task_user_manager

Краткое описание:
Проект разработан для создания и управления пользовательскими аккаунтами. 
С их помощью пользователи могут создовать, изменять, удалять, читать свои задачи. 

Установка проекта.

Kлонируйте репозиторий 
HTTPS:
git clone https://github.com/AseevAlexandr/task_user_manager.git

Установите и активируйте виртуальное окружение:

python3 -m venv venv # Linux/MacOS создание виртуального окружения

python -m venv venv # Windows создание виртуального окружения

Активация виртуального окружения:

source venv/bin/activate # активация виртуального окружения

Установите зависимости:

pip install -r requirements.txt

Запуск локального сервера:

python3 manage.py runserver # Linux/MacOS

python manage.py runserver # Windows

Приложение Users доступно по ссылке http://127.0.0.1:8000/api/v2/users/
Позволяет создавать, изменять, удалять пользовательский аккаун

Приложение Tasks доступно по ссылке http://127.0.0.1:8000/api/v1/tasks/
Становится доступна после создания и авторизации пользовательского аккаунта.
Позволяет создавать, изменять, удалять, просматривать список задач.

Выполнение тестирования:

python3 manage.py test # Linux/MacOS

python manage.py test # Windows

Для тестирования отдельного приложения :

python3 manage.py test tasks # Linux/MacOS

python manage.py test users # Windows

Документация проекта доступна по ссылке:

http://127.0.0.1:8000/docs/