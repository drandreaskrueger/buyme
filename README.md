# buyme v0.14
*Coinbase payments made easy.* Django app to buy time with BTC payments. The whole process.
  
= Learning how to include **Coinbase checkouts**, incl. properly reacting to webhook callback data. 

## Try it live:

(1) FRONTEND: **http://208.68.38.174:8000/buyme** to create the product & checkout.

(2) Get a free [coinbase sandbox](https://sandbox.coinbase.com/) account to pay with testnet3 coins. 

(3) BACKEND: http://208.68.38.174:8000/admin (user: tester, password: tipmeplease)

*Or* see [output/](output/) for some screenshots & logfiles.

## Quickstart

Prepare [server](_how-to/VPS.md):

    apt-get update && apt-get -y upgrade
    apt-get install -y sudo nano lynx tree screen dos2unix wget curl python-pip git 
    sudo pip install -U pip
    sudo pip install Django iptools requests jsonfield coinbase

Clone and configure this repo:

    git clone https://github.com/drandreaskrueger/buyme.git
    cd buyme
    nano buyme/configPrivate.py

Fill in your API_KEY and API_SECRET, see [configure.md#api-key-for-coinbase-access] (https://github.com/drandreaskrueger/buyme/blob/master/_how-to/configure.md#api-key-for-coinbase-access). Forget email, for now. 

Initialize Django & DB: 

    python manage.py makemigrations buyme
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py collectstatic
    
Run server: 

	python manage.py runserver 0.0.0.0:8000
	
Open in browser (change to your IP address):

* http://208.68.38.174:8000/buyme = the app
* http://208.68.38.174:8000/admin = admin pages for the DB
    
## More information:
[![diagrams and more](_how-to/img/thumbs.png)](_how-to/README.md)

See [_how-to/README.md](_how-to/README.md) for diagrams, and manuals.

## You might want to edit:
* in [buyme/](buyme/) = django *app*:
  * [configPrivate.py](buyme/configPrivate.py) = coinbase KEY (*), and email (optional). 
  * [config.py](buyme/config.py) = constants that influence some app properties.
  * [templates/](buyme/templates/) = html template of buyme/-page with form
* [djangosite/settings.py](djangosite/settings.py) = django project which loads the app

(*) = MUST EDIT. Keep everything else unchanged, for a starter.
## donation ware!
(C) 2016 Andreas Krueger  
If you like this, show it: [BTC] 1JjSXcUKEmZGTvdC9BGbM6RrkGVdApape5  
