# smsmailing
Service for management mailings.

###  Автор: Дерябин Евгений

### Технологии:

- celery==5.3.1
- Django==4.2.3
- djangorestframework==3.14.0
- drf-yasg==1.21.6
- flower==2.0.0
- phonenumberslite==8.13.15
- redis==4.6.0

### Установка
1. Скачать репозиторий:   ```git clone git@github.com:fersus85/smsmailing.git```
2. Перейти в папку проекта, создать и активировать виртуальное окружение: ```python -m venv venv```, ```source venv/bin/activate```
3. Установить необходимые зависимости: ```pip install -r requirements.txt```
4. Сделать миграции ```python manage.py makemigrations```, ```python manage.py migrate```
5. Запустить сервер ```python manage.py runserver```
6. celery ```celery -A notification_service worker -l info```
### Навигация
```http://127.0.0.1:8000/docs/``` - документация swagger
```http://127.0.0.1:8000/api/v1/mailings/``` - все рассылки, с возможностью добавлять новые
```http://127.0.0.1:8000/api/v1/mailings/stats/```статистика по рассылкам
```http://127.0.0.1:8000/api/v1/mailings/{pk}/detstats/``` статистика выбранной рассылки
```http://127.0.0.1:8000/api/v1/clients/``` - все клиенты, с возможностью добавлять новых
```http://127.0.0.1:8000/api/v1/messages/``` - все сообщения, с возможностью добавлять новые

#### Дополнительно написаны тесты (для запуска ```python manage.py test```)
#### По адресу /docs/ открывается swagerUI
