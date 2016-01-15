# Create project and app
You DO NOT have to do all this. I have just documented all steps, how I have created the django app.

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

### URLs to try on localhost:
#### localhost (for dev'ing in eclipse)

GET:  
[http://localhost:8000/buyme/](http://localhost:8000/buyme/)

[http://localhost:8000/buyme/hook/1111111111823472893/](http://localhost:8000/buyme/hook/1111111111823472893/)  
[http://localhost:8000/admin](http://localhost:8000/admin)

POST:
  
    curl -X POST -d "name=Andreas%20Krueger&project=buyme" http://localhost:8000/buyme/hook/1111111111823472893/  
    curl -X POST -d "name=Andreas%20Krueger&project=buyme" http://localhost:8000/buyme/hook/9999999911111263534/

BTW: On windows, I got ``curl`` via [chocolatey](https://chocolatey.org/):

    choco install curl 

### copy to linux VPS
copy all files to linux VPS (TODO: git clone ...), then

    cd /var/www/djangoproject
    python manage.py makemigrations buyme
    python manage.py migrate
    
	python manage.py runserver 0.0.0.0:8000
	
	
### URLs in the cloud 

http://208.68.38.174:8000/buyme

http://208.68.38.174:8000/buyme/hook/1111111111823472893/
http://208.68.38.174:8000/admin

curl -X POST -d "name=Andreas%20Krueger&project=buyme" http://208.68.38.174:8000/buyme/hook/1111111111823472893/  
curl -X POST -d "name=Andreas%20Krueger&project=buyme" http://208.68.38.174:8000/buyme/hook/9999999911111263534/

Of course - replace the 208.68.38.174 with *your IP address*.


