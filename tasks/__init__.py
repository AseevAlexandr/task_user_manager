"""
Пакет task выполняет функции-создания, изменения,чтения,удаления пользовательскими задачами.
В него из приложения users интегрирована модель User для того чтобы каждый авторизованный пользователь
мог управлять своими задачами, но не имел доступа к задачам других пользователей

Oсновные файлы приложения:
- models.py хранит модель Tasks.
- serializers.py сериализует(преобразовывает) модель для её дальнейшего использования.
- view.py содержит класс IsAuthorOnly позволяющий только автору получать доступ к своим задачам. И класс TaskViewSet для обработки задачи пользователем.
- tests.py содержит тесты функций этого приложения. Для запуска тестирования выполните команду:
python manage.py test tasks для windows
python3 manage.py test tasks для linux/macOS
"""
