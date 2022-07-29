python -m pip install --upgrade pip
pip install django
django-admin startproject project_1
cd project_1
python manage.py startapp blog
python manage.py migrate
python manage.py runserver
pip install pillow