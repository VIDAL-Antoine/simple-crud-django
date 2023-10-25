# Simple CRUD Django

Cette application est un simple CRUD fait en Django. Pour la partie Django le code est inspiré par [Débutez avec le framework Django](https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django). Il y a divers ajouts comme le CSS ou les termes qui ont été changés.

## Lancement de l'application

- Télécharger avec par exemple `git clone`
- Installez les packages avec `pip install -r requirements.txt`
- Allez dans le répertoire de l'application avec `cd merchex`
- Lancer avec `python manage.py runserver`
- L'application est disponible sur `http://127.0.0.1:8000`
 

## Fonctionnement de l'application

Il s'agit d'une simple interface où l'on peut faire ce que l'on appelle un CRUD (Create, Read, Update, Delete). Ici cela est possible sur deux entités : les groupes (de musiques) et les listings. Les listings ont besoin d'un groupe pour exister, la fonctionnalité de clé étrangère a donc été également été testée.
