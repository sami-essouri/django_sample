# django_sample project with forms:


  - pip install - r requirements.txt to install all requirements for this project
  - python manage.py makemigrations app to create a migration file detecting any model changes
  - python manage.py migrate to execute the migration
  - python manage.py runserver to run server


# JWT Token:

Using postman, go to those urls after creating a user to generate a token:
- http://127.0.0.1:8000/api/token/
- http://127.0.0.1:8000/api/token/refresh/
- http://127.0.0.1:8000/api/token/verify/

