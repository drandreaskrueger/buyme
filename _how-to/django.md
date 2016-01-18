# Create project and app
You DO NOT have to do all this. I have just documented all steps, how I have created the **django app**.

### create django project & app within eclipse
Within eclipse (4.5):

* new ... django project ...
* djangosite ...
* django ... custom command ... startapp buyme

#### create database 
* django ... make migrations ... buyme
* django ... migrate

The ``createsuperuser`` command has to be run in a CMD-shell in the djangosite folder:

    python manage.py createsuperuser

to set the username & password for the admin area.


### (alternative) create django project & app *manually*
This was not recognized as a django project in Eclipse later, so I did *not* do it this way. But still ...:

    django-admin.exe startproject djangosite
    cd djangosite

    python manage.py startapp buyme
    python manage.py makemigrations buyme
    python manage.py migrate
    
    python manage.py createsuperuser

    python manage.py runserver 0.0.0.0:8000

Later I found out this would have been the way to *make it a Django project*:  

eclipse:
* right click on project
  * PyDev ... set as Django project
  * Properties ... PyDev - Django: 
    * Django manage.py: ``manage.py``
	* Django settings module: ``djangosite.settings``


### register app in project

    djangosite/urls.py
    	url(r'^buyme/', include('buyme.urls')),

    djangosite/settings.py
        INSTALLED_APPS = (...,
        'buyme')

    buyme/urls.py
    	url(r'^$', 'buyme.views.home', name='home'),


### start server

Eclipse ... Run ... Run as ... PyDev: Django
or

    python manage.py runserver 0.0.0.0:8000


### On linux VPS
See [#quickstart](../#quickstart). If DB gets corrupted, a fresh start goes like this:
    
	rm db.sqlite3
	rm buyme/migrations/*
	
    python manage.py makemigrations buyme
    python manage.py migrate
    python manage.py createsuperuser
    
	python manage.py runserver 0.0.0.0:8000
	
