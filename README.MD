# Simple CRUD Django

⚠️ The text / UI of the application is only available in French ⚠️

This application is a simple CRUD made in Django. For the Django part, the code is inspired by [Débutez avec le framework Django](https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django). There are various additions such as CSS or terms that have been changed.

## Launching the application

- Download with `git clone`.
- Install packages with `pip install -r requirements.txt`.
- Go to the application directory with `cd merchex`.
- Run with `python manage.py runserver`.
- The application is available at `http://127.0.0.1:8000`
 
## How the application works

This is a simple interface where you can perform what's known as a CRUD (Create, Read, Update, Delete). Here, this is possible on two entities: groups (of music) and listings. Listings need a group to exist, so the foreign key functionality has also been tested.
